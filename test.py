from gentopia.config.config import Config

x = Config.load("gentopia/agent/agent.yaml")
print(x)

from gentopia.config.agent_config import AgentConfig

x = AgentConfig("gentopia/agent/agent.yaml")
a = x.get_agent()
print(a)
print(a.tools.tools['Wikipedia'].description)
print(a.tools.generate_worker_prompt())
print(x)
