const fs = require("node:fs");

function calcDistance (arrayOne, arrayTwo) {

    const group1Sorted = arrayOne.sort();
    const group2Sorted = arrayTwo.sort();
    
    const distances = group1Sorted.map((locID, i) => Math.abs( locID - group2Sorted[i]));
  
    return distances.reduce((totalDist, dist) => totalDist + dist);
}

function calcSimilarity (arrayOne, arrayTwo) {

    const similarity = arrayOne.map((locID1) => 
        locID1 * arrayTwo.reduce((countID, locID2) => 
            (locID2 === locID1 ? countID + 1 : countID), 0)
    );

    return similarity.reduce((totalSim, sim) => totalSim + sim);
}

fs.readFile("input.txt", "utf8", (err, data) => {
    if (err) {
        console.error(err);
        return;
    } 
    
    const lines = data.split('\n');

    const group1 = [];
    const group2 = [];

    for (line of lines) {
        group1.push(Number(line.split(/\s/).filter(n => n)[0]));
        group2.push(Number(line.split(/\s/).filter(n => n)[1]));
    }

    // part 1
    console.log("Total distance between the two lists:", calcDistance(group1, group2));

    // part 2
    console.log("Similarity score of the two lists:", calcSimilarity(group1, group2));
});
