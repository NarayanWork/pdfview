def main():
    n = int(input("Enter number of activities: "))

    if n < 1 or n > 26:
        print("Please enter between 1 and 26 activities.")
        return

    duration = []
    for i in range(n):
        d = int(input(f"Activity {chr(ord('A') + i)} duration: "))
        if d < 0:
            print("Duration cannot be negative.")
            return
        duration.append(d)

    # Forward pass (assumes activities occur sequentially)
    es = [0] * n
    ef = [0] * n
    for i in range(n):
        es[i] = 0 if i == 0 else ef[i - 1]
        ef[i] = es[i] + duration[i]

    project_duration = ef[-1]

    # Backward pass
    ls = [0] * n
    lf = [0] * n
    lf[-1] = project_duration
    ls[-1] = lf[-1] - duration[-1]

    for i in range(n - 2, -1, -1):
        lf[i] = ls[i + 1]
        ls[i] = lf[i] - duration[i]

    print("\nActivity  Duration  ES  EF  LS  LF  Slack")
    for i in range(n):
        slack = ls[i] - es[i]
        print(f"{chr(ord('A') + i):<9} {duration[i]:<9} {es[i]:<3} {ef[i]:<3} "
              f"{ls[i]:<3} {lf[i]:<3} {slack}")

    print("\nCritical Path:", " -> ".join(chr(ord('A') + i) for i in range(n)))
    print("Project Duration:", project_duration)
    print("\nNote: This simplified CPM program assumes all activities occur sequentially.")


if __name__ == "__main__":
    main()
