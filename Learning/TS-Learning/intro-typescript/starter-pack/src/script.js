(function () {
    var _a;
    (_a = document.getElementById('guess-form')) === null || _a === void 0 ? void 0 : _a.addEventListener("submit", compareUserGuess);
    function compareUserGuess(event) {
        event.preventDefault();
        var secretNumber = generateSecretNumber();
        var userNumber = document.getElementById('guess').value;
        var userNumberAsNumber = parseInt(userNumber, 10);
        if (secretNumber === userNumberAsNumber) {
            alert("Awesome! Your number ".concat(userNumber, " was correct. You can be named many things, hungry not being one of them."));
        }
        else {
            alert("Bummer... You guessed ".concat(userNumber, " and the secret number was ").concat(secretNumber, "."));
        }
    }
    function generateSecretNumber() {
        var secretNumber = getRandomArbitrary(1, 22);
        return secretNumber;
    }
    function getRandomArbitrary(min, max) {
        return Math.round(Math.random() * (max - min) + min);
    }
})();
