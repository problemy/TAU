import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import java.util.ArrayList;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class ToDoListTest {
	
	private ToDoList todolist = new ToDoList();
	
	@Before
	public void setUp() {
		todolist.setTopic("Mat's task list");
		todolist.createTask("Task1");
		System.out.println("before");
	}
	@After
	public void tearDown() {
		todolist = null;
	}
	
	@Test
	public void ToDoListTest1() {
		
		assertEquals("Mat's task list", todolist.getTopic());

	}
	@Test
	public void ToDoListTest2() {
		
		assertNotNull(todolist.getTasks());

	}
	@Test
	public void ToDoListTest3() {
		ArrayList<Task> tasks = todolist.getTasks();
		int result = tasks.size();
		assertEquals(1, result);

	}
	

}
