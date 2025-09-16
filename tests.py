from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("\n\n\n")
print("Result for current directory:")
print (get_files_info("calculator", "."))
print("\n\n")
print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))
print("\n\n")
print("Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"))
print("\n\n")
print("Result for '../' directory:")
print(get_files_info("calculator", "../"))
print("\n\n\n")



print("get_file_content result for 'main.py'")
print(get_file_content("calculator", "main.py"))
print("\n\n")
print("get_file_content result for 'pkg/calculator.py'")
print(get_file_content("calculator", "pkg/calculator.py"))
print("\n\n")
print("get_file_content result for '/bin/cat'")
print(get_file_content("calculator", "/bin/cat"))
print("\n\n")
print("get_file_content result for 'pkg/does_not_exists.py'")
print(get_file_content("calculator", "pkg/does_not_exists.py"))