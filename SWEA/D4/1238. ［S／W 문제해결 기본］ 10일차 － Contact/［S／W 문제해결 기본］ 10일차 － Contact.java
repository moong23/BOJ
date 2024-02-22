import java.util.*;

public class Solution {

	    public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);
	        int testcase = 10; // Number of test cases

	        // Iterate over each test case
	        for (int i = 0; i < testcase; i++) {
	            Map<Integer, List<Integer>> contact = new HashMap<>(); // Dictionary to store contacts
	            List<Integer> visited = new ArrayList<>(); // List to store visited nodes
	            List<Integer> current = new ArrayList<>(); // List to store current nodes
	            List<Integer> bigList = new ArrayList<>(); // List to store the second largest element in each iteration

	            // Read input
	            int length = scanner.nextInt(); // Length of the list
	            int start = scanner.nextInt(); // Starting node
	            int[] str = new int[length]; // List of contacts
	            for (int j = 0; j < length; j++) {
	                str[j] = scanner.nextInt();
	            }

	            int idx = 0;
	            // Create the contact map
	            while (idx < length) {
	                int key = str[idx];
	                int value = str[idx + 1];
	                if (contact.containsKey(key)) {
	                    contact.get(key).add(value);
	                } else {
	                    List<Integer> tempList = new ArrayList<>();
	                    tempList.add(value);
	                    contact.put(key, tempList);
	                }
	                idx += 2;
	            }

	            // Initialize current list with the starting node and mark it as visited
	            current.add(start);
	            visited.add(start);

	            int big = -1; // Initialize the second largest element as -1

	            // Main loop to traverse the graph
	            while (!current.isEmpty()) {
	                big = -1; // Reset the second largest element to -1 for each iteration
	                List<Integer> deletion = new ArrayList<>(); // List to store nodes to be deleted from current
	                List<Integer> addition = new ArrayList<>(); // List to store nodes to be added to current

	                // Iterate over each node in current
	                for (int cu : current) {
	                    deletion.add(cu); // Mark the current node for deletion

	                    // Check if the current node has contacts
	                    if (contact.containsKey(cu)) {
	                        List<Integer> target = contact.get(cu); // Get the contacts of the current node
	                        // Iterate over each contact of the current node
	                        for (int x : target) {
	                            // Check if the contact is not in current and not visited yet
	                            if (!current.contains(x) && !visited.contains(x)) {
	                                big = Math.max(big, x); // Update the second largest element if necessary
	                                visited.add(x); // Mark the contact as visited
	                                addition.add(x); // Mark the contact for addition to current
	                            }
	                        }
	                    }
	                }

	                // Remove nodes marked for deletion from current
	                for (int x : deletion) {
	                    current.remove((Integer) x);
	                }

	                // Add nodes marked for addition to current
	                current.addAll(addition);

	                bigList.add(big); // Store the second largest element for the current iteration
	            }

	            // Output the result for the current test case
	            System.out.println("#" + (i + 1) + " " + bigList.get(bigList.size() - 2));
	        }
	    }
	}
