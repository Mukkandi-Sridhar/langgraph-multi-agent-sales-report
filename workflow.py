from langgraph.graph import StateGraph, END
from state import SalesReportState
from agents import (
    data_collector,
    data_processor,
    chart_generator,
    report_generator,
    error_handler,
)
from router import route_next_step


def build_workflow():
    graph = StateGraph(SalesReportState)

    graph.add_node("data_collector", data_collector)
    graph.add_node("data_processor", data_processor)
    graph.add_node("chart_generator", chart_generator)
    graph.add_node("report_generator", report_generator)
    graph.add_node("error_handler", error_handler)

    for node in [
        "data_collector",
        "data_processor",
        "chart_generator",
        "report_generator",
        "error_handler",
    ]:
        graph.add_conditional_edges(node, route_next_step)

    graph.set_entry_point("data_collector")
    return graph.compile()
