from workflow import build_workflow
from state import SalesReportState


if __name__ == "__main__":
    app = build_workflow()

    initial_state: SalesReportState = {
        "request": "Q1-Q2 Sales Report",
        "raw_data": None,
        "processed_data": None,
        "chart_config": None,
        "report": None,
        "errors": [],
        "next_action": "collect",
    }

    final_state = app.invoke(initial_state)
    print(final_state["report"])
