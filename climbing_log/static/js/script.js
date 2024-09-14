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
// Get the difficulty value from the hidden span
const gradeDropdownEditValue = document.getElementById(
  "difficulty-for-dropdown"
);
// if difficulty-for-dropdown exists get text content
if (gradeDropdownEditValue) {
  const gradeDropdownEditValueText = gradeDropdownEditValue.textContent.trim();
  // Populate dropdown options
  grades.forEach((grade) => {
    const option = document.createElement("option");
    option.value = grade;
    option.textContent = grade;
    // Set the selected attribute for the grade that was in difficulty-for-dropdown
    if (grade === gradeDropdownEditValueText) {
      option.selected = true;
    }
    // add to difficulty element
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
const deleteSessionModal = document.getElementById("deleteSessionModal");
const submitDeleteSessionFormButton = document.getElementById(
  "submitDeleteSessionForm"
);
let currentSessionId = null;
// Listen for button clicks to open the modal
if (deleteSessionModal) {
  deleteSessionModal.addEventListener("show.bs.modal", function (event) {
    // Button that triggered the modal
    const button = event.relatedTarget;

    // Extract the session ID from the button's data attribute
    currentSessionId = button.getAttribute("data-session-id");
  });
}
// When the user confirms the deletion
if (submitDeleteSessionFormButton) {
  submitDeleteSessionFormButton.addEventListener("click", function () {
    if (currentSessionId) {
      // Find the correct form using the session ID and submit it
      const deleteForm = document.getElementById(
        `deleteSessionForm-${currentSessionId}`
      );
      if (deleteForm) {
        deleteForm.submit();
      }
    }
  });
}
const deleteClimbModal = document.getElementById("deleteClimbModal");
const submitDeleteClimbFormButton = document.getElementById(
  "submitDeleteClimbForm"
);
let currentClimbId = null;
// Listen for button clicks to open the modal
if (deleteClimbModal) {
  deleteClimbModal.addEventListener("show.bs.modal", function (event) {
    // Button that triggered the modal
    const button = event.relatedTarget;

    // Extract the climb ID from the button's data attribute
    currentClimbId = button.getAttribute("data-climb-id");
  });
}
// When the user confirms the deletion
if (submitDeleteClimbFormButton) {
  submitDeleteClimbFormButton.addEventListener("click", function () {
    if (currentClimbId) {
      // Find the correct form using the climb ID and submit it
      const deleteForm = document.getElementById(
        `deleteClimbForm-${currentClimbId}`
      );
      if (deleteForm) {
        deleteForm.submit();
      }
    }
  });
}
