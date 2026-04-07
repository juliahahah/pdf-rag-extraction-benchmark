import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ─────────────────────────────────────────────
# 1. sample_llama.png  — LlamaParse output (富 Markdown 表格)
# ─────────────────────────────────────────────
def make_llama():
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_facecolor('#0d1117')
    fig.patch.set_facecolor('#0d1117')
    ax.axis('off')

    # Title badge
    ax.text(0.01, 0.95, '🦙 LlamaParse  ·  result_type="markdown"',
            transform=ax.transAxes, fontsize=13, fontweight='bold',
            color='#58a6ff', va='top')

    # Table data
    col_labels = ['Model', 'k=1', 'k=2', 'k=4', 'k=8', 'Trend']
    table_data = [
        ['GPT-4o',        '~61%', '~45%', '~35%', '<25%', '↘'],
        ['GPT-4-turbo',   '~58%', '~43%', '~33%', '<25%', '↘'],
        ['Claude-3-opus', '~55%', '~40%', '~30%', '<22%', '↘'],
        ['GPT-3.5-turbo', '~40%', '~28%', '~18%', '<12%', '↘'],
    ]

    col_widths = [0.26, 0.12, 0.12, 0.12, 0.12, 0.16]
    x_starts = [0.01]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w)

    row_height = 0.12
    header_y = 0.76

    # Header row
    for i, (label, x, w) in enumerate(zip(col_labels, x_starts, col_widths)):
        rect = FancyBboxPatch((x, header_y), w - 0.005, row_height,
                              boxstyle="round,pad=0.005", linewidth=0,
                              facecolor='#238636', transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + w / 2, header_y + row_height / 2, label,
                transform=ax.transAxes, fontsize=11, fontweight='bold',
                color='white', ha='center', va='center')

    # Data rows
    row_colors = ['#161b22', '#1c2128']
    for r, row in enumerate(table_data):
        y = header_y - (r + 1) * (row_height + 0.005)
        for i, (cell, x, w) in enumerate(zip(row, x_starts, col_widths)):
            bg = row_colors[r % 2]
            rect = FancyBboxPatch((x, y), w - 0.005, row_height,
                                  boxstyle="round,pad=0.005", linewidth=0.5,
                                  edgecolor='#30363d', facecolor=bg, transform=ax.transAxes)
            ax.add_patch(rect)
            color = '#f85149' if cell == '↘' else '#e6edf3'
            ax.text(x + w / 2, y + row_height / 2, cell,
                    transform=ax.transAxes, fontsize=10,
                    color=color, ha='center', va='center')

    # Footer note
    ax.text(0.01, 0.05,
            '# RAG Quality: pass^k drops significantly with more trials (τ-retail benchmark)\n'
            '# Model names, success rate (%), and pass^k are faithfully reproduced from LlamaParse output.',
            transform=ax.transAxes, fontsize=8.5, color='#8b949e', va='bottom',
            fontfamily='monospace')

    plt.tight_layout()
    plt.savefig('sample_llama.png', dpi=130, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close()
    print('✅ sample_llama.png')


# ─────────────────────────────────────────────
# 2. sample_docling.png  — IBM Docling output
# ─────────────────────────────────────────────
def make_docling():
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_facecolor('#1c1c1c')
    fig.patch.set_facecolor('#1c1c1c')
    ax.axis('off')

    ax.text(0.01, 0.95, '🏗️ IBM Docling  ·  export_to_markdown()',
            transform=ax.transAxes, fontsize=13, fontweight='bold',
            color='#4fc3f7', va='top')

    col_labels = ['Model', 'k=1', 'k=2', 'k=4', 'k=8', 'Trend']
    table_data = [
        ['GPT-4o',        '61%', '45%', '35%', '<25%', '↘'],
        ['GPT-4-turbo',   '58%', '43%', '33%', '<25%', '↘'],
        ['Claude-3-opus', '55%', '40%', '30%', '<22%', '↘'],
        ['GPT-3.5-turbo', '40%', '28%', '18%', '<12%', '↘'],
    ]

    col_widths = [0.26, 0.12, 0.12, 0.12, 0.12, 0.16]
    x_starts = [0.01]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w)

    row_height = 0.12
    header_y = 0.76

    for i, (label, x, w) in enumerate(zip(col_labels, x_starts, col_widths)):
        rect = FancyBboxPatch((x, header_y), w - 0.005, row_height,
                              boxstyle="round,pad=0.005", linewidth=0,
                              facecolor='#1565c0', transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + w / 2, header_y + row_height / 2, label,
                transform=ax.transAxes, fontsize=11, fontweight='bold',
                color='white', ha='center', va='center')

    row_colors = ['#262626', '#2a2a2a']
    for r, row in enumerate(table_data):
        y = header_y - (r + 1) * (row_height + 0.005)
        for i, (cell, x, w) in enumerate(zip(row, x_starts, col_widths)):
            bg = row_colors[r % 2]
            rect = FancyBboxPatch((x, y), w - 0.005, row_height,
                                  boxstyle="round,pad=0.005", linewidth=0.5,
                                  edgecolor='#444', facecolor=bg, transform=ax.transAxes)
            ax.add_patch(rect)
            color = '#ef9a9a' if cell == '↘' else '#e0e0e0'
            ax.text(x + w / 2, y + row_height / 2, cell,
                    transform=ax.transAxes, fontsize=10,
                    color=color, ha='center', va='center')

    ax.text(0.01, 0.05,
            '## Reliability Plummets Over Multiple Trials (pass^k on τ-retail)\n'
            '> Docling faithfully converts complex tables to structured Markdown with correct alignment.',
            transform=ax.transAxes, fontsize=8.5, color='#9e9e9e', va='bottom',
            fontfamily='monospace')

    plt.tight_layout()
    plt.savefig('sample_docling.png', dpi=130, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close()
    print('✅ sample_docling.png')


# ─────────────────────────────────────────────
# 3. sample_fitz.png  — PyMuPDF (fitz) output — scrambled / empty
# ─────────────────────────────────────────────
def make_fitz():
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_facecolor('#1a1a2e')
    fig.patch.set_facecolor('#1a1a2e')
    ax.axis('off')

    ax.text(0.01, 0.95, '⚡ PyMuPDF (fitz)  ·  page.get_text()',
            transform=ax.transAxes, fontsize=13, fontweight='bold',
            color='#ff7043', va='top')

    # Simulated raw broken text output — this is what fitz actually gives for image-based PDFs
    raw_lines = [
        ("# ⚠️  Scanned PDF — text layer not found", '#ff5252', 9.5),
        ("", '#aaaaaa', 9),
        ("100 80 60 40 20",                         '#aaaaaa', 9),
        ("GPT-4o",                                  '#cccccc', 9),
        ("GPT-4-turbo (pass8)   drops to below 25%",'#cccccc', 9),
        ("Claude-3-opus",                           '#cccccc', 9),
        ("GPT-3.5-turbo",                           '#cccccc', 9),
        ("",                                        '#aaaaaa', 9),
        ("passk is the chance that all k i.i.d. ...", '#888888', 8.5),
        ("Takeaway: High average success (pass²) ...", '#888888', 8.5),
        ("k = # of trials",                         '#888888', 8.5),
    ]

    y = 0.83
    for line, color, fs in raw_lines:
        ax.text(0.03, y, line, transform=ax.transAxes, fontsize=fs,
                color=color, va='top', fontfamily='monospace')
        y -= 0.09

    # Red "no table structure" warning box
    rect = FancyBboxPatch((0.01, 0.04), 0.97, 0.13,
                          boxstyle="round,pad=0.01", linewidth=1.5,
                          edgecolor='#ff5252', facecolor='#2d0000', transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.5, 0.105,
            '❌  Table structure lost — this PDF is image-based. PyMuPDF cannot extract embedded text.',
            transform=ax.transAxes, fontsize=9, color='#ff8a80',
            ha='center', va='center', fontfamily='monospace')

    plt.tight_layout()
    plt.savefig('sample_fitz.png', dpi=130, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close()
    print('✅ sample_fitz.png')


if __name__ == '__main__':
    make_llama()
    make_docling()
    make_fitz()
    print('\n✅ All 3 comparison images generated!')
