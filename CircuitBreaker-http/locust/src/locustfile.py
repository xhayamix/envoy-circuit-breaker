from locust import HttpUser, TaskSet, task, constant, constant_pacing, between


class TestUser(TaskSet):   
    @task(1)
    def scenario(self):
        self.hello("aaa")

    def hello(self, name: str):
        self.client.get(
            "/hello?name=" + name
        )
        
class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [TestUser]