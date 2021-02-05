from apm_agent_utils.instrumentation import InstrumentationBuilder


builder = InstrumentationBuilder("Test")
builder.add_instrument("example.logic.logic1", r"^hello.*")
builder.add_instrument("example.logic.logic1", r"^TestClass.*")
builder.add_instrument("example.logic.sub_logic.logic2", r".*")

Test = builder.create_instrument()