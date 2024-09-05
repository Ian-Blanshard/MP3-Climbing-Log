// list of climbing grades to populate the difficulty dropdown for form in log_climb.html
const grades = [
  "4",
  "5",
  "5+",
  "6A",
  "6A+",
  "6B",
  "6B+",
  "6C",
  "6C+",
  "7A",
  "7A+",
  "7B",
  "7B+",
  "7C",
  "7C+",
  "8A",
  "8A+",
  "8B",
  "8B+",
  "8C",
  "8C+",
  "9A",
];
// assign difficulty dropdown element to v variable
const gradeDropdown = document.getElementById('difficulty');
// for loop to populate dropdown
if (gradeDropdown) {
  grades.forEach(grade => {
    const option = document.createElement('option');
    option.textContent = grade;
    gradeDropdown.appendChild(option);
});
}


