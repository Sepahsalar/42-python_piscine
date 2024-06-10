def ft_tqdm(lst) -> None:
    total = len(lst)
    bar_width = 63

    def show_progress(iteration, total):
        prog = iteration / total
        prog_bar = '=' * int(bar_width * prog)
        remaining = ' ' * (bar_width - len(prog_bar))
        percentage = prog * 100
        return f"{percentage:.0f}%|[{prog_bar}{remaining}]|{iteration}/{total}"

    for i, item in enumerate(lst):
        prog = show_progress(i + 1, total)
        print(prog, end='\r')
        yield item
    print()
