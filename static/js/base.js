// function myFunction() {
/* Get the text field */
// var copyText = document.getElementById("myInput");

/* Select the text field */
// copyText.select();
// copyText.setSelectionRange(0, 99999); /*For mobile devices*/

/* Copy the text inside the text field */
// document.execCommand("copy");

/* Alert the copied text */
// alert("Copied the text: " + copyText.value);
// }

function myFunction() {
    var copyText = document.getElementById("myInput");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");

    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied: " + copyText.value;
}

function outFunc() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
}

