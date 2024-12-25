function solve(input) {
    const farmersCount = parseInt(input.shift());
    const farmersInput = input.splice(0, farmersCount);
    const farmers = farmersInput.reduce((farmersObj, entry) => {
        let [name, location, tasks] = entry.split(' ');
        tasks = tasks.split(',');

        farmersObj[name] = { location, tasks };

        return farmersObj;
    }, {});

    input.forEach(entry => {
        const line = entry.split(' / ');
        const command = line.shift();

        if (command === "End") return;

        const name = line[0];
        if (!farmers[name]) {
            // If the farmer is not found, skip the command.
            console.error(`Farmer ${name} does not exist.`);
            return;
        }

        switch (command) {
            case 'Execute': {
                const [_, workArea, task] = line;
                if (farmers[name].location === workArea && farmers[name].tasks.includes(task)) {
                    console.log(`${name} has executed the task: ${task}!`);
                } else {
                    console.log(`${name} cannot execute the task: ${task}.`);
                }
                break;
            }
            case 'Change Area': {
                const [_, newArea] = line;
                farmers[name].location = newArea;
                console.log(`${name} has changed their work area to: ${newArea}`);
                break;
            }
            case 'Learn Task': {
                const [_, newTask] = line;
                if (farmers[name].tasks.includes(newTask)) {
                    console.log(`${name} already knows how to perform ${newTask}.`);
                } else {
                    farmers[name].tasks.push(newTask);
                    console.log(`${name} has learned a new task: ${newTask}.`);
                }
                break;
            }
        }
    });

    // Final Output
    Object.keys(farmers).forEach(name => {
        const farmer = farmers[name];
        farmer.tasks.sort(); // Alphabetically sort tasks
        console.log(
            `Farmer: ${name}, Area: ${farmer.location}, Tasks: ${farmer.tasks.join(', ')}`
        );
    });
}