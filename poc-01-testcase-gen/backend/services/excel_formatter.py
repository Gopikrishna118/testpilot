import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

_COLUMNS = [
    "test_id", "module", "scenario", "preconditions",
    "test_steps", "expected_result", "priority", "test_type",
    "traceability", "notes",
]
_HEADER_FILL = PatternFill("solid", fgColor="1F4E79")
_HEADER_FONT = Font(color="FFFFFF", bold=True)
_REVIEW_FILL = PatternFill("solid", fgColor="FFF2CC")  # yellow highlight for NEEDS REVIEW


class ExcelFormatter:
    @staticmethod
    def write(test_cases: list[dict[str, Any]], output_dir: str) -> str:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Test Cases"

        for col_idx, col in enumerate(_COLUMNS, start=1):
            cell = ws.cell(row=1, column=col_idx, value=col.replace("_", " ").title())
            cell.fill = _HEADER_FILL
            cell.font = _HEADER_FONT
            cell.alignment = Alignment(horizontal="center")

        for row_idx, tc in enumerate(test_cases, start=2):
            for col_idx, col in enumerate(_COLUMNS, start=1):
                value = tc.get(col, "")
                if isinstance(value, list):
                    value = "\n".join(f"{i + 1}. {s}" for i, s in enumerate(value))
                cell = ws.cell(row=row_idx, column=col_idx, value=value)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                if col == "notes" and isinstance(value, str) and "NEEDS REVIEW" in value:
                    cell.fill = _REVIEW_FILL

        ws.freeze_panes = "A2"
        for col_cells in ws.columns:
            ws.column_dimensions[col_cells[0].column_letter].width = 25

        disclaimer = wb.create_sheet("Disclaimer")
        disclaimer["A1"] = "AI-GENERATED OUTPUT — REQUIRES HUMAN REVIEW BEFORE USE"
        disclaimer["A1"].font = Font(bold=True, color="FF0000")

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        out_path = os.path.join(output_dir, f"testcases_{timestamp}.xlsx")
        wb.save(out_path)
        return out_path
