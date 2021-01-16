import java.util.ArrayList;

public class ToDoList {

		public String topic;
		private ArrayList<Task> Tasks = new ArrayList<Task>();
		public String getTopic() {
			return topic;
		}

		public void setTopic(String topic) {
			this.topic = topic;
		}
		
		public Task createTask(String name){
			Task t = new Task(name);
			this.Tasks.add(t);		
			return t;
		}
		
		
		public ArrayList<Task> getTasks(){
			return this.Tasks;
		}
		

}
