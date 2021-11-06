use std::env;
use std::io::{BufWriter, Write};

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Usage: program path_to_file");
        return;
    }

    let fname = args.get(1).unwrap();

    println!("Writing to {}", fname);

    let file = std::fs::File::create(fname).expect("Can't create file");
    let mut writer = BufWriter::new(file);

    let up_bound = 10u32.pow(9);

    // "pseudo-random" order
    for n in (0..up_bound).rev() {
        write!(writer, "+79{:09}\n", n).unwrap();
    }

    writer.flush().unwrap();
}
