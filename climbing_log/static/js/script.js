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
const gradeDropdown = document.getElementById("difficulty");
// for loop to populate dropdown
if (gradeDropdown) {
  grades.forEach((grade) => {
    const option = document.createElement("option");
    option.textContent = grade;
    gradeDropdown.appendChild(option);
  });
}

// code for confirmation of delete user modal
// create variables for two elements involved in modal/form
const submitDeleteUserFormButton = document.getElementById(
  "submitDeleteUserForm"
);
const deleteUserForm = document.getElementById("deleteUserForm");
//check if elements exist before adding event listeners - stops errors if not on this page
if (submitDeleteUserFormButton && deleteUserForm) {
  //add event listener to modal button so this button can submit delete user form
  submitDeleteUserFormButton.addEventListener("click", function () {
    deleteUserForm.submit();
  });
}

// code for confirmation of delete session modal
// create variables for two elements involved in modal/form
const submitDeleteSessionFormButton = document.getElementById(
  "submitDeleteSessionForm"
);
const deleteSessionForm = document.getElementById("deleteSessionForm");
//check if elements exist before adding event listeners - stops errors if not on this page
if (submitDeleteSessionFormButton && deleteSessionForm) {
  //add event listener to modal button so this button can submit delete session form
  submitDeleteSessionFormButton.addEventListener("click", function () {
    deleteSessionForm.submit();
  });
}

// code for confirmation of delete climb modal
// create variables for two elements involved in modal/form
const submitDeleteClimbFormButton = document.getElementById(
  "submitDeleteClimbForm"
);
const deleteClimbForm = document.getElementById("deleteClimbForm");
//check if elements exist before adding event listeners - stops errors if not on this page
if (submitDeleteClimbFormButton && deleteClimbForm) {
  //add event listener to modal button so this button can submit delete session form
  submitDeleteClimbFormButton.addEventListener("click", function () {
    deleteClimbForm.submit();
  });
}
