document.addEventListener('focus', function (event) {
    if (event.target.tagName.toLowerCase() !== 'textarea') return;
    autoResize(event.target);
  }, true);
  
  document.addEventListener('input', function (event) {
    if (event.target.tagName.toLowerCase() !== 'textarea') return;
    autoResize(event.target);
  }, false);
  
  document.addEventListener('blur', function (event) {
    if (event.target.tagName.toLowerCase() !== 'textarea') return;
    event.target.style.height = '50px'; // Set to default or min height on losing focus
  }, true);
  
  function autoResize(textarea) {
    textarea.style.height = 'auto'; // Reset the height
    textarea.style.height = textarea.scrollHeight + 'px'; // Set the height to scroll height
  }
  

  document.getElementById('predict').addEventListener('click', function() {
    document.getElementById('myForm').submit();
});

document.getElementById('delete-speech').addEventListener('click', function() {
  document.getElementById('speech-box').value = '';
});
