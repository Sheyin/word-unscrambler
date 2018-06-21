// If the user selects "yes, there are known letters", then the additional form is shown.
// Otherwise, those blanks remain hidden from view.
function getKnownLetters(knownNode) {
	var known = knownNode.value;
	var length = document.getElementById('length').value;

	if (known == 'True') {
		var letterBlanks = '';
		for (i=0; i<length; i++) {
			idName = 'letter' + i;
			letterBlanks += ' <input type="text" name=idName class="knownInput" maxlength="1" size="1" /> '
		}
		var formText = 'What letters are known?: <br>' + letterBlanks + '<br>';
		document.getElementById('knownLetterEntry').innerHTML=formText;
	}

	else {
		document.getElementById('knownLetterEntry').innerHTML='';
	}
}

// This reads each of the "known" letters and packages them into an array to be sent with the request.
function bundleKnownLetters() {
	var knownSpaces = document.getElementsByClassName('knownInput');
	for (i=0; i<document.getElementById('length').value; i++) {
		knownLetters = document.getElementById('knownLettersBox');
		if (knownSpaces[i].value == '') {
			knownLetters.value += '_';
		}
		else {
			knownLetters.value += knownSpaces[i].value;
		}
		// When done reading each space, should set it to "disabled" so it is not sent in the request.
		// But it's not quite working.
		// knownLetters.innerHTML = ' <input type="text" name=idName class="knownInput" maxlength="1" size="1" disabled /> '

	}
}

// This clears all the fields and resets values to default.
function resetForm() {
	// store old letters in cookie
	//writeCookie(document.getElementById('letters').value);
	document.getElementById('letters').value = '';
	document.getElementById('length').value = '';
	document.getElementById('unknownLetters').checked = true;
	document.getElementById('knownLetters').checked = false;
	document.getElementById('knownLetterEntry').innerHTML = '';
	document.getElementById('knownLettersBox').value = '';
}


// If the length changes, validate input and reset the "known letters"
function resetPartial() {
	checkLength();
	document.getElementById('unknownLetters').checked = true;
	document.getElementById('knownLetters').checked = false;
	document.getElementById('knownLetterEntry').innerHTML = '';
	document.getElementById('knownLettersBox').value = '';
}


// If the user does not enter enough scrambled letters to match the length of
// the word to find, then the length of the word to find will be updated to the
// lesser value (since it cannot be greater than the maximum letters given)
function checkLength() {
	var lengthGiven = document.getElementById('length').value;
	var lengthString = document.getElementById('letters').value.length;

	if (lengthGiven > lengthString) {
		document.getElementById('length').value = lengthString;
	}
}

// This function is not implemented yet - just copied some older code to use as a blueprint
// TODO: Fix this - lacking expiry date, way to track ~5-6 last used letters, etc.
function writeCookie(letterPool) {
	// get time data
	var d = new Date();
	//d.setFullYear(year);
	var append = "letters=" + letterPool;
	//var cookieExpiry = "expires=" + d.toUTCString();
	//var combinedCookie = append + cookieExpiry + ";path=/";
	//document.cookie = combinedCookie;

	// For debugging until I remember how to do this
	console.log("Cookie written: " + document.cookie);
}
