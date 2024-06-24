# def write_records_to_file(filename, records):
#     with open(filename, 'w') as file:
#         for record in records:
#             file.write(','.join(map(str, record)) + '\n')

# def main():
#     records = [
#         [1, 'Vinay', 80, 75, 90],
#         [2, 'Samir', 85, 90, 88],
#         [3, 'Abc', 70, 65, 75],
#         [4, 'Def', 92, 88, 95],
#         [5, 'Chal', 78, 82, 80]
#     ]

#     write_records_to_file('record.txt', records)
#     print("Records have been written to record.txt")

# if __name__ == "__main__":
#     main()



def calculate_percentage(sub1_marks, sub2_marks, sub3_marks):
    total_marks = sub1_marks + sub2_marks + sub3_marks
    percentage = (total_marks / 300) * 100
    return round(percentage, 2)


def process_records(input_file, output_file):
    with open(input_file, 'r') as file:
        with open(output_file, 'w') as result_file:
            for line in file:
                parts = line.strip().split(',')
                r_no = parts[0]
                name = parts[1]
                sub1_marks = int(parts[2])
                sub2_marks = int(parts[3])
                sub3_marks = int(parts[4])
                percentage = calculate_percentage(sub1_marks, sub2_marks, sub3_marks)
                result_file.write(f"{r_no},{name},{percentage}%\n")

def main():
    process_records('record.txt', 'result.txt')
    print("Percentage calculated and written to result.txt")

if __name__ == "__main__":
    main()
