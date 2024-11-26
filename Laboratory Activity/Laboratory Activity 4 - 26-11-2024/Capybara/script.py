from Capybara import Capybara

capybara1 = Capybara("Biscoff", "M", 5)
capybara2 = Capybara("Cocoa", "F", 3)

test_cases = {
    1: capybara1,
    2: capybara2
}

test_case = int(input("Enter the test case number: "))
selected_capybara = test_cases.get(test_case, None)

print(f"Test Case {test_case}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
    