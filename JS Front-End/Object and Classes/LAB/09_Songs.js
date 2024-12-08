function solve(input){
    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }
    }

    let songs = [];
    let number_of_songs = input.shift();
    let type_of_song = input.pop();

    for (let i = 0; i< number_of_songs; i++) {
        let [type,name,time] = input[i].split('_');
        let song = new Song(type,name,time);
        songs.push(song);
    }

    if (type_of_song === 'all') {
        songs.forEach((s) => console.log(s.name));
    } 
    else {
        let filtered_songs = songs.filter( (s) => s.type === type_of_song);
        filtered_songs.forEach( (s) => console.log(s.name))
    }
}

solve([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite'])