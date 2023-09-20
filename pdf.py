import time
import AppKit
from PyPDF2 import PdfReader

pdf_file_path = '/Users/mertpolat/Downloads/Docker Üzerinde MongoDB Cluster ve Metric Toplama İşlemleri.pdf'

pdf_reader = PdfReader(pdf_file_path)

total_pages = len(pdf_reader.pages)

scroll_interval = 15

app = AppKit.NSApplication.sharedApplication()
window = app.mainWindow()

# Check if the main window exists
if window is not None:
    window.makeFirstResponder()

for page_num in range(total_pages):
    should_scroll = True

    if should_scroll and window is not None:
        window.scrollWheel(AppKit.NSEventModifierFlags.CommandKeyModifierFlag, 1)

    time.sleep(scroll_interval)
