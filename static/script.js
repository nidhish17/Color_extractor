async function copyToClipboard(textToCopy) {
    // Navigator clipboard api needs a secure context (https)
    if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(textToCopy);
    } else {
        // Use the 'out of viewport hidden text area' trick
        const textArea = document.createElement("textarea");
        textArea.value = textToCopy;

        // Move textarea out of the viewport so it's not visible
        textArea.style.position = "absolute";
        textArea.style.left = "-999999px";

        document.body.prepend(textArea);
        textArea.select();

        try {
            document.execCommand('copy');
        } catch (error) {
            console.error(error);
        } finally {
            textArea.remove();
        }
    }
}


const copy_icon = document.querySelectorAll(".copy-icon");

copy_icon.forEach(function (element){
    element.addEventListener("click", function(){
        //copy to clipboard
        copyToClipboard(element.title);
        // console.log(element.title)
    })

    element.addEventListener("mouseover", function(){
        //copy to clipboard
        console.log("hovering")
        element.style.cursor = "pointer"
        // console.log(element.title)
    })

})

const submitbtn = document.querySelector("#form-submit-btn");
const form = document.getElementById('color-form');

const colorPalletSection = document.querySelector("#color-pallet");


submitbtn.addEventListener("click", function (e){
  if (form.checkValidity()){
    // console.log("i was clicked")
  submitbtn.classList.add("disabled")
    submitbtn.value = "Uploading..."
  }

});


document.addEventListener("DOMContentLoaded", function () {
  // Scroll to the colorPalletSection
  colorPalletSection.scrollIntoView({ behavior: "smooth" });
});


