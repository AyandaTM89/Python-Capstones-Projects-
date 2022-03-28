// import packages
import java.util.Scanner;

// defining main class
public class Poised {

	// defining main method
	public static void main(String[] args) {
		
		// menu options for the user to select from
		Scanner input = new Scanner(System.in);
		int choice;
		System.out.println("--MENU--\n");
		System.out.println("1. Add NEW PROJECT");
		System.out.println("2. Add ARCHITECT");
		System.out.println("3. Add CONTRACTOR");
		System.out.println("4. FINALISE PROJECT ");
		System.out.println("5. EDIT");
		System.out.println("0. EXIT");
		System.out.println("Enter choice between(0 - 5):");
		choice = input.nextInt();
		
		// if user selects 1 they will have to fill in New project details
		if (choice == 1){
			System.out.println("NEW PROJECT FORM \n");
			
			//New Project details
			// data types and all the attributes
			System.out.println("Enter Project ID: ");
			int ProjectNumber = input.nextInt();
			 
			System.out.println("Enter Project Name: ");
			String ProjectName = input.nextLine();
			
			System.out.println("Enter Building Type: ");
			String BuildingType = input.nextLine();
			
			System.out.println("Enter Project Address: ");
			String ProjectAdrress = input.next();
			
			System.out.println("Enter ERF Number: ");
			double ERF_Number = input.nextDouble();
			
			System.out.println("Enter Fee Charged: ");
			double FeeCharged = input.nextDouble();
			
			System.out.println("Enter Amount Paid: ");
			double AmountPaid = input.nextDouble();
			
			System.out.println("Enter DeadLine Date: ");
			String DeadlineDate = input.nextLine();

			//Architect details
			System.out.println("Enter Architect Name: ");
			String ArchitectName = input.nextLine();
			System.out.println("Enter Architect Cell Number: ");
			int ArchitectNumber = input.nextInt();
			System.out.println("Enter Architect Email Address: ");
			String ArchitectEmail = input.nextLine();
			System.out.println("Enter Architect Physical Address: ");
			String ArchitectAddress = input.nextLine();

			//Contractor details
			System.out.println("Enter Contractor ID: ");
			int ContractorID = input.nextInt();
			System.out.println("Enter Contractor Name: ");
			String ContractorName = input.nextLine();
			System.out.println("Enter Contractor Cell Number: ");
			int ContractorNumber = input.nextInt();
			System.out.println("Enter Contractor Email: ");
			String ContyractorEmail = input.nextLine();
			System.out.println("Enter Contractor Physical Address: ");
			String ContractorAddress = input.nextLine();

			//Customer Details
			System.out.println("Enter Customer ID: ");
			int CustomerID = input.nextInt();
			System.out.println("Enter Customer Name: ");
			String CustomerName = input.nextLine();
			System.out.println("Enter Customer Cell Number: ");
			int CustomerNumber = input.nextInt();
			System.out.println("Enter Customer Email: ");
			String CustomerEmail = input.nextLine();
			System.out.println("Enter Customer Physical Address: ");
			String CustomerAddress = input.nextLine();
			
			// constructor and the attributes of the objects
			Architect architecture = new Architect(ArchitectName, ArchitectNumber, ArchitectEmail, ArchitectAddress);
			Contractor contractor = new Contractor(ContractorID, ContractorName, ContractorNumber, ContyractorEmail, ContractorAddress);
			Customer customer = new Customer(CustomerID,CustomerName, CustomerNumber, CustomerEmail, CustomerAddress);
			
				
		}
		
		else if(choice == 2) {
			
			//Architect details
			System.out.println("ARCHITECT DETAILS \n");
			System.out.println("Enter Architect Name: ");
			String ArchitectName = input.nextLine();
			
			System.out.println("Enter Architect Cell Number: ");
			int ArchitectNumber = input.nextInt();
			
			System.out.println("Enter Architect Email Address: ");
			String ArchitectEmail = input.nextLine();
			
			System.out.println("Enter Architect Physical Address: ");
			String ArchitectAddress = input.nextLine();
			
			Architect architecture = new Architect(ArchitectName, ArchitectNumber, ArchitectEmail, ArchitectAddress);
		}
		
		else if(choice == 3) {
			
			System.out.println("CONTRACTOR DETAILS \n");
			//Contractor details
			System.out.println("Enter Contractor ID: ");
			int ContractorID = input.nextInt();
			System.out.println("Enter Contractor Name: ");
			String ContractorName = input.nextLine();
			System.out.println("Enter Contractor Cell Number: ");
			int ContractorNumber = input.nextInt();
			System.out.println("Enter Contractor Email: ");
			String ContyractorEmail = input.nextLine();
			System.out.println("Enter Contractor Physical Address: ");
			String ContractorAddress = input.nextLine();
			
			Contractor contractor = new Contractor(ContractorID, ContractorName, ContractorNumber, ContyractorEmail, ContractorAddress);
			
			
		}
		
		else if(choice == 4) {
			System.out.println("Enter a Project Number to Finalise: ");
			int ProjectNumber = input.nextInt();
			return;
		}
		
		else if (choice == 5) {
			// Editing Menu
			System.out.println("--EDITING OPTIONS--\n");
			System.out.println("1. CHANGE AMOUNT OF FEE PAID");
			System.out.println("2. CHANGE CONTRACTOR CONTACTS");
			System.out.println("3. CHANGE DUE DATE OF PROJECT");
			System.out.println("0. BACK");
			System.out.println("Enter Options between(0 - 3):");
			int options = input.nextInt();
			
				if (options == 1) {
					
					System.out.println("Please enter the new amout: ");
					double AmountPaid = input.nextDouble();
				}
				else if(options == 2) {
					
					System.out.println("Please enter new contrctors contacts");
					int ContractorNumber = input.nextInt();
				}
				else if (options == 3) {
					System.out.println("Enter DeadLine Date: ");
					String DeadlineDate = input.nextLine();
				}
				else if (options == 0) {
					System.exit(options);
				}
			
			
		}
		
		else if (choice == 0) {
			System.exit(choice);
		}
		
		
		
	}

}
