#!/usr/bin/env python3
"""
chunk_large_pdf.py - Intelligent PDF Chunking for Large Documents

Purpose: Handles large PDF files that exceed LLM context limits by extracting
         text and splitting into manageable chunks with preserved traceability.

Version: 1.0.0
Author: QA Automation Skill
Date: 2025-11-15

Features:
- Automatic size detection (file size and page count)
- Intelligent chunking strategies (by page, by size, by section)
- Text extraction with fallback methods
- Page number preservation for traceability
- Summary file generation
- Progress tracking
- Error handling and recovery

Usage:
    python3 chunk_large_pdf.py <pdf_file> [options]

Examples:
    # Auto-detect and chunk if needed
    python3 chunk_large_pdf.py requirements.pdf

    # Force chunking with custom chunk size
    python3 chunk_large_pdf.py requirements.pdf --chunk-size 50000 --force

    # Chunk by pages (10 pages per chunk)
    python3 chunk_large_pdf.py requirements.pdf --strategy pages --pages-per-chunk 10

    # Custom output directory
    python3 chunk_large_pdf.py requirements.pdf --output chunks/
"""

import sys
import os
import argparse
from pathlib import Path
from typing import List, Tuple, Optional
import re

# Try importing PDF libraries with graceful fallback
PDF_LIBRARY = None
try:
    import PyPDF2
    PDF_LIBRARY = "PyPDF2"
except ImportError:
    pass

if PDF_LIBRARY is None:
    try:
        import pdfplumber
        PDF_LIBRARY = "pdfplumber"
    except ImportError:
        pass

if PDF_LIBRARY is None:
    try:
        from pypdf import PdfReader
        PDF_LIBRARY = "pypdf"
    except ImportError:
        pass


class PDFChunker:
    """Handles intelligent chunking of large PDF documents."""

    # Thresholds for determining if chunking is needed
    MAX_FILE_SIZE_MB = 5  # Maximum file size before chunking (MB)
    MAX_PAGES = 50        # Maximum pages before chunking
    MAX_CHARS = 100000    # Maximum characters before chunking (~25k tokens)

    # Default chunking parameters
    DEFAULT_CHUNK_SIZE = 50000      # Characters per chunk
    DEFAULT_PAGES_PER_CHUNK = 10    # Pages per chunk
    OVERLAP_CHARS = 500             # Character overlap between chunks for context

    def __init__(self, pdf_path: str, output_dir: Optional[str] = None,
                 force: bool = False, verbose: bool = False):
        """
        Initialize PDF chunker.

        Args:
            pdf_path: Path to the PDF file
            output_dir: Output directory for chunks (default: <pdf_name>_chunks/)
            force: Force chunking even if file is small
            verbose: Enable verbose logging
        """
        self.pdf_path = Path(pdf_path)
        self.force = force
        self.verbose = verbose

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        # Setup output directory
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = self.pdf_path.parent / f"{self.pdf_path.stem}_chunks"

        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Statistics
        self.stats = {
            'file_size_mb': 0,
            'total_pages': 0,
            'total_chars': 0,
            'chunks_created': 0,
            'chunking_needed': False,
            'chunking_reason': None
        }

    def log(self, message: str, force: bool = False):
        """Print log message if verbose or force."""
        if self.verbose or force:
            print(message)

    def check_if_chunking_needed(self) -> Tuple[bool, str]:
        """
        Check if PDF needs chunking.

        Returns:
            (needs_chunking, reason)
        """
        if self.force:
            return True, "Force flag enabled"

        # Check file size
        file_size_mb = self.pdf_path.stat().st_size / (1024 * 1024)
        self.stats['file_size_mb'] = file_size_mb

        if file_size_mb > self.MAX_FILE_SIZE_MB:
            return True, f"File size ({file_size_mb:.1f} MB) exceeds {self.MAX_FILE_SIZE_MB} MB"

        # Check page count (requires PDF library)
        if PDF_LIBRARY:
            try:
                page_count = self._get_page_count()
                self.stats['total_pages'] = page_count

                if page_count > self.MAX_PAGES:
                    return True, f"Page count ({page_count}) exceeds {self.MAX_PAGES} pages"
            except Exception as e:
                self.log(f"Warning: Could not check page count: {e}")

        return False, "File is within acceptable limits"

    def _get_page_count(self) -> int:
        """Get total number of pages in PDF."""
        if PDF_LIBRARY == "PyPDF2":
            with open(self.pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                return len(reader.pages)

        elif PDF_LIBRARY == "pdfplumber":
            import pdfplumber
            with pdfplumber.open(self.pdf_path) as pdf:
                return len(pdf.pages)

        elif PDF_LIBRARY == "pypdf":
            from pypdf import PdfReader
            reader = PdfReader(self.pdf_path)
            return len(reader.pages)

        raise RuntimeError("No PDF library available")

    def extract_text(self) -> List[Tuple[int, str]]:
        """
        Extract text from PDF page by page.

        Returns:
            List of (page_number, text) tuples
        """
        if PDF_LIBRARY is None:
            raise RuntimeError(
                "No PDF library installed. Install one of: PyPDF2, pdfplumber, pypdf\n"
                "  pip install PyPDF2  # or\n"
                "  pip install pdfplumber  # or\n"
                "  pip install pypdf"
            )

        self.log(f"Extracting text using {PDF_LIBRARY}...")
        pages_text = []

        try:
            if PDF_LIBRARY == "PyPDF2":
                with open(self.pdf_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for i, page in enumerate(reader.pages, start=1):
                        text = page.extract_text() or ""
                        pages_text.append((i, text))
                        self.log(f"  Extracted page {i}/{len(reader.pages)}")

            elif PDF_LIBRARY == "pdfplumber":
                import pdfplumber
                with pdfplumber.open(self.pdf_path) as pdf:
                    for i, page in enumerate(pdf.pages, start=1):
                        text = page.extract_text() or ""
                        pages_text.append((i, text))
                        self.log(f"  Extracted page {i}/{len(pdf.pages)}")

            elif PDF_LIBRARY == "pypdf":
                from pypdf import PdfReader
                reader = PdfReader(self.pdf_path)
                for i, page in enumerate(reader.pages, start=1):
                    text = page.extract_text() or ""
                    pages_text.append((i, text))
                    self.log(f"  Extracted page {i}/{len(reader.pages)}")

        except Exception as e:
            raise RuntimeError(f"Failed to extract text from PDF: {e}")

        # Calculate total characters
        self.stats['total_chars'] = sum(len(text) for _, text in pages_text)
        self.log(f"Extracted {len(pages_text)} pages, {self.stats['total_chars']:,} characters", force=True)

        return pages_text

    def chunk_by_pages(self, pages_text: List[Tuple[int, str]],
                       pages_per_chunk: int = DEFAULT_PAGES_PER_CHUNK) -> List[dict]:
        """
        Chunk PDF by page count.

        Args:
            pages_text: List of (page_number, text) tuples
            pages_per_chunk: Number of pages per chunk

        Returns:
            List of chunk dictionaries
        """
        chunks = []

        for i in range(0, len(pages_text), pages_per_chunk):
            chunk_pages = pages_text[i:i + pages_per_chunk]

            # Combine text from pages
            chunk_text = "\n\n".join([
                f"[Page {page_num}]\n{text}"
                for page_num, text in chunk_pages
            ])

            chunks.append({
                'chunk_id': len(chunks) + 1,
                'start_page': chunk_pages[0][0],
                'end_page': chunk_pages[-1][0],
                'page_count': len(chunk_pages),
                'char_count': len(chunk_text),
                'text': chunk_text
            })

        return chunks

    def chunk_by_size(self, pages_text: List[Tuple[int, str]],
                      chunk_size: int = DEFAULT_CHUNK_SIZE) -> List[dict]:
        """
        Chunk PDF by character count with intelligent breaks.

        Args:
            pages_text: List of (page_number, text) tuples
            chunk_size: Target characters per chunk

        Returns:
            List of chunk dictionaries
        """
        chunks = []
        current_chunk = []
        current_size = 0

        for page_num, text in pages_text:
            page_text = f"[Page {page_num}]\n{text}"
            page_size = len(page_text)

            # If adding this page would exceed chunk size and we have content
            if current_size + page_size > chunk_size and current_chunk:
                # Save current chunk
                chunk_text = "\n\n".join(current_chunk)
                chunks.append({
                    'chunk_id': len(chunks) + 1,
                    'start_page': self._extract_start_page(current_chunk[0]),
                    'end_page': page_num - 1,
                    'page_count': len(current_chunk),
                    'char_count': len(chunk_text),
                    'text': chunk_text
                })

                # Start new chunk with overlap from previous chunk
                if chunks:
                    overlap = self._get_overlap(current_chunk[-1], self.OVERLAP_CHARS)
                    current_chunk = [overlap, page_text]
                    current_size = len(overlap) + page_size
                else:
                    current_chunk = [page_text]
                    current_size = page_size
            else:
                current_chunk.append(page_text)
                current_size += page_size

        # Add final chunk
        if current_chunk:
            chunk_text = "\n\n".join(current_chunk)
            chunks.append({
                'chunk_id': len(chunks) + 1,
                'start_page': self._extract_start_page(current_chunk[0]),
                'end_page': pages_text[-1][0],
                'page_count': len(current_chunk),
                'char_count': len(chunk_text),
                'text': chunk_text
            })

        return chunks

    def chunk_by_sections(self, pages_text: List[Tuple[int, str]],
                          max_section_size: int = DEFAULT_CHUNK_SIZE) -> List[dict]:
        """
        Chunk PDF by detected sections/headings.

        Args:
            pages_text: List of (page_number, text) tuples
            max_section_size: Maximum characters per section before splitting

        Returns:
            List of chunk dictionaries
        """
        # Section detection patterns (common heading formats)
        section_patterns = [
            r'^#{1,6}\s+(.+)$',           # Markdown headings
            r'^([A-Z][A-Z\s]+)$',          # ALL CAPS headings
            r'^\d+\.\s+([A-Z].+)$',        # Numbered sections (1. Introduction)
            r'^\d+\.\d+\s+([A-Z].+)$',     # Subsections (1.1 Overview)
        ]

        chunks = []
        current_section = []
        current_size = 0
        current_start_page = pages_text[0][0] if pages_text else 1

        for page_num, text in pages_text:
            lines = text.split('\n')
            page_content = f"[Page {page_num}]\n"

            for line in lines:
                # Check if line is a section heading
                is_heading = any(re.match(pattern, line.strip())
                               for pattern in section_patterns)

                # If we hit a section heading and current section is large enough
                if is_heading and current_size > max_section_size // 2:
                    # Save current section
                    chunk_text = page_content + "\n".join(current_section)
                    chunks.append({
                        'chunk_id': len(chunks) + 1,
                        'start_page': current_start_page,
                        'end_page': page_num,
                        'char_count': len(chunk_text),
                        'text': chunk_text
                    })

                    # Start new section
                    current_section = [line]
                    current_size = len(line)
                    current_start_page = page_num
                else:
                    current_section.append(line)
                    current_size += len(line)

        # Add final section
        if current_section:
            chunk_text = "\n".join(current_section)
            chunks.append({
                'chunk_id': len(chunks) + 1,
                'start_page': current_start_page,
                'end_page': pages_text[-1][0] if pages_text else 1,
                'char_count': len(chunk_text),
                'text': chunk_text
            })

        # If section-based chunking didn't find sections, fall back to size-based
        if len(chunks) <= 1:
            self.log("No clear sections detected, falling back to size-based chunking")
            return self.chunk_by_size(pages_text, max_section_size)

        return chunks

    def _extract_start_page(self, page_text: str) -> int:
        """Extract page number from page text header."""
        match = re.match(r'\[Page (\d+)\]', page_text)
        return int(match.group(1)) if match else 1

    def _get_overlap(self, text: str, overlap_size: int) -> str:
        """Get last N characters as overlap for context."""
        if len(text) <= overlap_size:
            return text
        return "...(previous context)...\n" + text[-overlap_size:]

    def save_chunks(self, chunks: List[dict], strategy: str):
        """Save chunks to individual files."""
        self.log(f"\nSaving {len(chunks)} chunks to {self.output_dir}/", force=True)

        for chunk in chunks:
            # Generate filename
            filename = f"chunk_{chunk['chunk_id']:03d}_pages_{chunk['start_page']}-{chunk['end_page']}.txt"
            filepath = self.output_dir / filename

            # Create chunk header
            header = f"""{'=' * 80}
CHUNK {chunk['chunk_id']} of {len(chunks)}
{'=' * 80}
Source PDF: {self.pdf_path.name}
Pages: {chunk['start_page']}-{chunk['end_page']} ({chunk.get('page_count', 'N/A')} pages)
Characters: {chunk['char_count']:,}
Chunking Strategy: {strategy}
{'=' * 80}

"""

            # Write chunk file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header)
                f.write(chunk['text'])

            self.log(f"  ✓ Saved {filename} ({chunk['char_count']:,} chars)")

        self.stats['chunks_created'] = len(chunks)

    def create_summary(self, chunks: List[dict], strategy: str, reason: str):
        """Create summary file with chunking information."""
        summary_path = self.output_dir / "00_CHUNKING_SUMMARY.txt"

        summary = f"""{'=' * 80}
PDF CHUNKING SUMMARY
{'=' * 80}

SOURCE FILE INFORMATION:
  File: {self.pdf_path.name}
  Path: {self.pdf_path.absolute()}
  Size: {self.stats['file_size_mb']:.2f} MB
  Total Pages: {self.stats['total_pages']}
  Total Characters: {self.stats['total_chars']:,}

CHUNKING INFORMATION:
  Chunking Needed: {self.stats['chunking_needed']}
  Reason: {reason}
  Strategy Used: {strategy}
  Total Chunks Created: {len(chunks)}

CHUNK DETAILS:
"""

        for chunk in chunks:
            summary += f"""
  Chunk {chunk['chunk_id']}:
    File: chunk_{chunk['chunk_id']:03d}_pages_{chunk['start_page']}-{chunk['end_page']}.txt
    Pages: {chunk['start_page']}-{chunk['end_page']}
    Characters: {chunk['char_count']:,}
"""

        summary += f"""
{'=' * 80}
USAGE INSTRUCTIONS:

Process chunks sequentially when analyzing requirements:
  1. Read chunk_001_pages_X-Y.txt first
  2. Extract requirements/information
  3. Move to next chunk
  4. Combine findings from all chunks

Each chunk includes:
  - Page number markers for traceability
  - Context overlap between chunks (when applicable)
  - Source information in header

{'=' * 80}
Generated: {self._get_timestamp()}
PDF Library: {PDF_LIBRARY}
{'=' * 80}
"""

        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary)

        self.log(f"  ✓ Saved summary: {summary_path.name}", force=True)

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def process(self, strategy: str = "auto",
                chunk_size: int = DEFAULT_CHUNK_SIZE,
                pages_per_chunk: int = DEFAULT_PAGES_PER_CHUNK) -> dict:
        """
        Main processing method.

        Args:
            strategy: Chunking strategy ("auto", "pages", "size", "sections")
            chunk_size: Characters per chunk (for "size" strategy)
            pages_per_chunk: Pages per chunk (for "pages" strategy)

        Returns:
            Statistics dictionary
        """
        self.log(f"{'=' * 80}", force=True)
        self.log(f"PDF Chunking Tool - Processing: {self.pdf_path.name}", force=True)
        self.log(f"{'=' * 80}", force=True)

        # Check if chunking is needed
        needs_chunking, reason = self.check_if_chunking_needed()
        self.stats['chunking_needed'] = needs_chunking
        self.stats['chunking_reason'] = reason

        if not needs_chunking:
            self.log(f"\n✓ No chunking needed: {reason}", force=True)
            self.log(f"  File size: {self.stats['file_size_mb']:.2f} MB", force=True)
            self.log(f"  Pages: {self.stats.get('total_pages', 'Unknown')}", force=True)
            self.log(f"\nYou can process this PDF directly with the LLM.", force=True)
            return self.stats

        self.log(f"\n⚠ Chunking needed: {reason}", force=True)

        # Extract text
        pages_text = self.extract_text()

        # Determine strategy
        if strategy == "auto":
            # Auto-select based on file characteristics
            if self.stats['total_pages'] > 100:
                strategy = "pages"
                self.log("Auto-selected strategy: pages (large page count)")
            elif self.stats['total_chars'] > 200000:
                strategy = "sections"
                self.log("Auto-selected strategy: sections (large text content)")
            else:
                strategy = "size"
                self.log("Auto-selected strategy: size")

        # Apply chunking strategy
        self.log(f"\nApplying '{strategy}' chunking strategy...", force=True)

        if strategy == "pages":
            chunks = self.chunk_by_pages(pages_text, pages_per_chunk)
        elif strategy == "size":
            chunks = self.chunk_by_size(pages_text, chunk_size)
        elif strategy == "sections":
            chunks = self.chunk_by_sections(pages_text, chunk_size)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        # Save chunks
        self.save_chunks(chunks, strategy)

        # Create summary
        self.create_summary(chunks, strategy, reason)

        # Final report
        self.log(f"\n{'=' * 80}", force=True)
        self.log(f"CHUNKING COMPLETE", force=True)
        self.log(f"{'=' * 80}", force=True)
        self.log(f"  Original: {self.stats['total_pages']} pages, {self.stats['total_chars']:,} chars", force=True)
        self.log(f"  Created: {len(chunks)} chunks", force=True)
        self.log(f"  Output: {self.output_dir}/", force=True)
        self.log(f"\nNext steps:", force=True)
        self.log(f"  1. Review: {self.output_dir}/00_CHUNKING_SUMMARY.txt", force=True)
        self.log(f"  2. Process chunks sequentially in the skill workflow", force=True)
        self.log(f"{'=' * 80}", force=True)

        return self.stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Intelligent PDF chunking for large documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto-detect and chunk if needed
  python3 chunk_large_pdf.py requirements.pdf

  # Force chunking with page-based strategy
  python3 chunk_large_pdf.py requirements.pdf --strategy pages --pages-per-chunk 10 --force

  # Size-based chunking with custom chunk size
  python3 chunk_large_pdf.py requirements.pdf --strategy size --chunk-size 50000

  # Section-based intelligent chunking
  python3 chunk_large_pdf.py requirements.pdf --strategy sections

  # Custom output directory
  python3 chunk_large_pdf.py requirements.pdf --output my_chunks/

Chunking Strategies:
  auto     - Automatically select best strategy (default)
  pages    - Chunk by page count (good for large PDFs)
  size     - Chunk by character count (good for consistent sizing)
  sections - Chunk by detected sections/headings (best quality)
"""
    )

    parser.add_argument('pdf_file', help='Path to PDF file to process')

    parser.add_argument('--strategy', '-s',
                       choices=['auto', 'pages', 'size', 'sections'],
                       default='auto',
                       help='Chunking strategy (default: auto)')

    parser.add_argument('--chunk-size', '-c', type=int,
                       default=PDFChunker.DEFAULT_CHUNK_SIZE,
                       help=f'Characters per chunk for size/sections strategy (default: {PDFChunker.DEFAULT_CHUNK_SIZE})')

    parser.add_argument('--pages-per-chunk', '-p', type=int,
                       default=PDFChunker.DEFAULT_PAGES_PER_CHUNK,
                       help=f'Pages per chunk for pages strategy (default: {PDFChunker.DEFAULT_PAGES_PER_CHUNK})')

    parser.add_argument('--output', '-o',
                       help='Output directory for chunks (default: <pdf_name>_chunks/)')

    parser.add_argument('--force', '-f', action='store_true',
                       help='Force chunking even if file is small')

    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    try:
        # Create chunker
        chunker = PDFChunker(
            pdf_path=args.pdf_file,
            output_dir=args.output,
            force=args.force,
            verbose=args.verbose
        )

        # Process PDF
        stats = chunker.process(
            strategy=args.strategy,
            chunk_size=args.chunk_size,
            pages_per_chunk=args.pages_per_chunk
        )

        # Exit with appropriate code
        sys.exit(0 if stats['chunking_needed'] else 0)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user", file=sys.stderr)
        sys.exit(130)

    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
