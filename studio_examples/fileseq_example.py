import shutil

import fileseq


def move_file_sequence(source, destination):
    """
    Moves a sequence of files from source to destination

    Args:
        source (str): Sequence filepath, eg, /path/to/file.####.png
        destination (str): Destination, using a single # for frames, eg,
            /path/to/renamed.#.png
    """
    src_sequence = fileseq.findSequenceOnDisk(source)
    dst_sequence = fileseq.FileSequence(destination.replace("#", "1-1#"))
    dst_sequence.setFrameSet(src_sequence.frameSet())
    for src_frame, dst_frame in zip(src_sequence, dst_sequence):
        shutil.move(src_frame, dst_frame)


if __name__ == '__main__':
    import os

    move_file_sequence(
        os.path.join(os.path.dirname(__file__), "sequence", "render.####.png"),
        os.path.join(os.path.dirname(__file__), "sequence", "example.#.png"),
    )
