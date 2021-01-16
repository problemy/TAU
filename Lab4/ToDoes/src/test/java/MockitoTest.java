import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.Date;

import org.junit.*;
import org.junit.Assert.*;
import org.mockito.Mock;

public class MockitoTest {
	Task  task;
	ToDoList todolist;
	@Before
	public void setUp() {
		task = mock(Task.class);
		todolist = mock(ToDoList.class);
	}
	
	@After
	public void tearDown() {
		todolist = null;
	}

	
	@Test
	public void test_mockito_todolist_topic() {
		when(todolist.getTopic()).thenReturn("topic");
	String topic = todolist.getTopic();
	assertEquals(topic, "topic");
		
	}
	
	@Test
	public void test_mockito_todolist_arraylist_tasks() {
		when(todolist.getTasks()).thenReturn(new ArrayList<Task>());
	ArrayList<Task> tasks  = todolist.getTasks();
	assertNotNull(tasks);
		
	}
	
	
	@Test
	public void test_mockito_todolist_createTask() {
		Task task = new Task("newtask");
		when(todolist.createTask("newtask")).thenReturn(task);
	assertEquals(task.getName(), "newtask");
		
	}
	
	@Test
	public void test_mockito_task_deadline() {
		Date currentDate = new Date();
		when(task.getDeadline()).thenReturn(currentDate);
	Date deadline = task.getDeadline();
	assertEquals(deadline, currentDate);
		
	}
	
	@Test
	public void test_mockito_task_name() {
		when(task.getName()).thenReturn("Name");
	String name = task.getName();
	assertEquals(name, "Name");
		
	}
	
	@Test
	public void test_mockito_task_user() {			
	String user  = "UserName";	
	task.setUser(user);
	when(task.getUser()).thenReturn(user);
	String userName = task.getUser();
	assertNotNull(userName);		
	}


}