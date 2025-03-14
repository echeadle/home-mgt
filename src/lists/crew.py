from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Lists():
	"""Lists Creating crew"""

	tasks_config = 'config/tasks.yaml'

	@agent
	def home_organizer(self) -> Agent:
		return Agent(
			config=self.agents_config['home_organizer'],
			verbose=True
		)

	@task
	def create_list_task(self) -> Task:
		return Task(
			config=self.tasks_config['create_list'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Lists crew"""

		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)
