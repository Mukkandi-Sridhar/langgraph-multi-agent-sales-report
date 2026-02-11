from state import SalesReportState


def data_collector(state: SalesReportState) -> SalesReportState:
    state["raw_data"] = {"sales": [100, 200, 150]}
    state["next_action"] = "process"
    return state


def data_processor(state: SalesReportState) -> SalesReportState:
    if not state["raw_data"]:
        state["errors"].append("No raw data found")
        state["next_action"] = "error"
        return state

    state["processed_data"] = {
        "total_sales": sum(state["raw_data"]["sales"])
    }
    state["next_action"] = "visualize"
    return state


def chart_generator(state: SalesReportState) -> SalesReportState:
    state["chart_config"] = {
        "type": "bar",
        "data": state["processed_data"]
    }
    state["next_action"] = "report"
    return state


def report_generator(state: SalesReportState) -> SalesReportState:
    state["report"] = (
        f"Total sales for period: {state['processed_data']['total_sales']}"
    )
    state["next_action"] = "complete"
    return state


def error_handler(state: SalesReportState) -> SalesReportState:
    state["report"] = "Workflow failed due to errors."
    state["next_action"] = "complete"
    return state
