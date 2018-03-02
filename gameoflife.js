var world = [
    [false, false, false],
    [true, true, true],
    [false, false, false]
]

var neighborsAlive = function (seed, myRow, myColumn) {
    var myself = seed[myRow][myColumn];
    var aliveCount = 0;
    for (var currentRow = Math.min(0, myRow -1); currentRow < myRow + 1; currentRow++) {
        for (var currentColumn = Math.min(0, myRow -1); currentColumn < myColumn + 1; currentColumn++) {
            if (seed[currentRow][currentColumn] === true){
                aliveCount = aliveCount + 1;
            };
        };
    };
    if (myself === true) {
        aliveCount -= 1;
    }
    return aliveCount;
};

var gameOfLife = function(seed) {
    var newWorld = [];
    for (var row = 0; row < seed.length; row++) {
        newWorld.push([]);
        for (var column = 0; column < seed[row].length; column++) {
            if (seed[row][column] === true) {
                if (neighborsAlive(seed, row, column) === 2 || neighborsAlive(seed, row, column) === 3) {
                    newWorld[row].push(true);
                } else {
                    newWorld[row].push(false);
                }    
            } else {
                if (neighborsAlive(seed, row, column) === 3){
                    newWorld[row].push(true);
                } else {
                    newWorld[row].push(false);
                }
            }
        }
    }
    return newWorld;
}

console.log(gameOfLife(world));