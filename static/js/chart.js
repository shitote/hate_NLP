const ctx = document.getElementById('myChart');
const nonHateProb = parseFloat(ctx.getAttribute('data-nonhate'));
const hateProb = parseFloat(ctx.getAttribute('data-hate'));



document.querySelector('textarea').addEventListener('focus', function () {
  // Ensure no dynamic resizing or unwanted styling
  this.style.height = '200px'; // Keep the height fixed
});


function updatePrediction(prediction) {
  const predictionBox = document.querySelector('.prediction');
  const verdict = document.querySelector('.verdict');

  verdict.textContent = prediction;

  // Add updated class for a brief animation effect
  predictionBox.classList.add('updated');

  // Remove the effect after a short delay
  setTimeout(() => {
    predictionBox.classList.remove('updated');
  }, 1000);
}
