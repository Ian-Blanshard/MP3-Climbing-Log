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

// // code for confirmation of delete session modal
// // create variables for two elements involved in modal/form
// const submitDeleteSessionFormButton = document.getElementById(
//   "submitDeleteSessionForm"
// );
// const deleteSessionForm = document.getElementById("deleteSessionForm");
// //check if elements exist before adding event listeners - stops errors if not on this page
// if (submitDeleteSessionFormButton && deleteSessionForm) {
//   //add event listener to modal button so this button can submit delete session form
//   submitDeleteSessionFormButton.addEventListener("click", function () {
//     deleteSessionForm.submit();
//   });
// }

const deleteSessionModal = document.getElementById("deleteSessionModal");
const submitDeleteSessionFormButton = document.getElementById(
  "submitDeleteSessionForm"
);

let currentSessionId = null;

// Listen for button clicks to open the modal
deleteSessionModal.addEventListener("show.bs.modal", function (event) {
  // Button that triggered the modal
  const button = event.relatedTarget;

  // Extract the session ID from the button's data attribute
  currentSessionId = button.getAttribute("data-session-id");
});

// When the user confirms the deletion
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

// code for confirmation of delete climb modal
// create variables for two elements involved in modal/form
// code for confirmation of delete climb modal
// query all the delete buttons and forms associated with climbs
// const deleteClimbForms = document.querySelectorAll("[id^='deleteClimbForm-']");
// const deleteClimbModalButtons = document.querySelectorAll(
//   "[id^='submitDeleteClimbForm-']"
// );

// // loop through each form and button to attach event listeners
// deleteClimbForms.forEach((form, index) => {
//   const submitButton = deleteClimbModalButtons[index];

//   //check if elements exist before adding event listeners
//   if (submitButton && form) {
//     // add event listener to modal button to submit the associated delete climb form
//     submitButton.addEventListener("click", function () {
//       form.submit();
//     });
//   }
// });
const deleteClimbModal = document.getElementById("deleteClimbModal");
const submitDeleteClimbFormButton = document.getElementById(
  "submitDeleteClimbForm"
);

let currentClimbId = null;

// Listen for button clicks to open the modal
deleteClimbModal.addEventListener("show.bs.modal", function (event) {
  // Button that triggered the modal
  const button = event.relatedTarget;

  // Extract the climb ID from the button's data attribute
  currentClimbId = button.getAttribute("data-climb-id");
});

// When the user confirms the deletion
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

