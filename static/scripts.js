// getKnownLetters(): If the user selects "yes, there are known letters",
// then this reveals an additional input box to enter that information.
// If the user selects "no" (default), the field remains hidden from view.
// Uses checkAreLettersBlank() to warn user to fill in letters first if
// the letters box is blank prior to clicking "yes".
function getKnownLetters(lettersAreKnownOption) {
  const known = lettersAreKnownOption.value;
  const length = document.getElementById("length").value;

  if (checkAreLettersBlank()) {
    // No letters given, halt execution
    return;
  }

  if (known == "True") {
    let letterBlanks = "";
    for (let i = 0; i < length; i++) {
      let idName = "letter" + i;
      let letterBlanksString =
        ' <input type="text" name="' +
        idName +
        '" class="knownLetterEntry" maxlength="1" /> ';
      letterBlanks += letterBlanksString;
    }
    const formText =
      '<div class="form-box">What letters are known?: <br />' +
      letterBlanks +
      "</div>";
    document.getElementById("knownLetterEntry").innerHTML = formText;
  } else {
    document.getElementById("knownLetterEntry").innerHTML = "";
  }
}

// populateNumbers(): Assuming user has just finished entering letters
// into #letters, it will count and prepopulate #numbers with the max
// value possible by default, so the user does not have to enter it manually.
function populateNumbers() {
  const length = document.getElementById("letters").value.length;
  const lengthNode = document.getElementById("length");
  lengthNode.value = length;
  resetPartial();
}

// packageAndSubmit(): Called when the user presses "Unscramble" and submits
// the form.  Gathers the form information and packages it before sending.
function packageAndSubmit() {
  const knownLettersRadio = document.getElementById("lettersKnownTrue");
  if (checkAreLettersBlank()) {
    // No letters given, halt execution
    return;
  }

  if (knownLettersRadio.checked) {
    bundleKnownLetters();
  }
  document.getElementById("inputForm").submit();
}

// bundleKnownLetters(): A helper function for packageAndSubmit().  This reads
// each of the "known" letters given when the form is submitted, and packages
// them into an array to be sent with the request.
function bundleKnownLetters() {
  const knownSpaces = document.getElementsByClassName("knownLetterEntry");
  for (let i = 0; i < document.getElementById("length").value; i++) {
    const knownLetters = document.getElementById("knownLettersBox");
    if (knownSpaces[i].value == "") {
      knownLetters.value += "_";
    } else {
      knownLetters.value += knownSpaces[i].value;
    }
    // When done reading each space, should set it to "disabled" so
    // it is not sent in the request.
    // Fixed how it is implemented, but I'm not entirely sure it is working,
    // or why I tried to add it in the first place.
    const knownInputBlanks = document.getElementsByClassName("knownInput");
    for (let i = 0; i < knownInputBlanks.length; i++) {
      knownInputBlanks[i].setAttribute("disabled", "");
    }
  }
}

// resetForm(): This clears all the fields and resets values
// to default values.  Used when "Clear form" button is pressed.
function resetForm() {
  document.getElementById("letters").value = "";
  document.getElementById("length").value = "";
  document.getElementById("lettersKnownFalse").checked = true;
  document.getElementById("lettersKnownTrue").checked = false;
  document.getElementById("knownLetterEntry").innerHTML = "";
  document.getElementById("knownLettersBox").value = "";
}

// resetPartial(): This provides a sanity check to make sure the
// requested length of the word is never larger than the
// maximum amount of letters given.  If the "length of the word"
// changes, it validates input and resets the "known letters"
// box and related fields.
function resetPartial() {
  checkLength();
  document.getElementById("lettersKnownFalse").checked = true;
  document.getElementById("lettersKnownTrue").checked = false;
  document.getElementById("knownLetterEntry").innerHTML = "";
  document.getElementById("knownLettersBox").value = "";
  document.getElementById("error-no-letters").innerHTML = "";
}

// checkLength(): A helper function for resetPartial().
// If the user does not enter enough scrambled letters to match the
// specified "length of the word to find", then the "length of the
// word to find" will be updated to match the maximum number of
// letters given, since there must be a letter given for every
// letter expected in the output.  Basically, a sanity check for input.
function checkLength() {
  const lengthGiven = document.getElementById("length").value;
  const lengthString = document.getElementById("letters").value.length;

  if (lengthGiven > lengthString) {
    document.getElementById("length").value = lengthString;
  }
}

// checkAreLettersBlank(): Helper function in getKnownLetters().
// When user clicks "yes" to knowing a letter's position, this checks
// to see if there are any letters already given since it would produce
// an odd blank prompt if none are given before clicking.
// Warns user if no letters are given; removes prompt if there are some.
function checkAreLettersBlank() {
  const length = document.getElementById("letters").value.length;
  const errorBox = document.getElementById("error-no-letters");

  if (length > 0) {
    errorBox.innerHTML = "";
    return false;
  } else {
    errorBox.innerHTML = "Please fill in the letters first.";
    document.getElementById("lettersKnownFalse").checked = true;
    return true;
  }
}
