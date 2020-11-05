package zad1;
import java.util.Date;

public class Task {
	private String name;
	private Date deadline;
	private String user;
	public Task(String name) {
		this.name = name;
		
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Date getDeadline() {
		return deadline;
	}
	public void setDeadline(Date deadline) {
		Date currentDate = new Date();
		if(deadline.before(currentDate)) {
			throw new IllegalArgumentException();
		}
			
		this.deadline = deadline;
	}
	public String getUser() {
		return user;
	}
	public void setUser(String user) {
		this.user = user;
	}
	
}
