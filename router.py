def route_next_step(state) -> str:
    return {
        "process": "data_processor",
        "visualize": "chart_generator",
        "report": "report_generator",
        "error": "error_handler",
        "complete": "END",
    }.get(state.get("next_action"), "END")
