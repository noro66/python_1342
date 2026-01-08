import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    arg_list = sys.argv
    arg_len = len(arg_list)
    if arg_len > 1:
        score_list = []
        try:
            for arg in arg_list[1:]:
                score_list.append(int(arg))

            total_players = len(score_list)
            lowest_score = min(score_list)
            highest_score = max(score_list)
            total_score = sum(score_list)
            average_score = total_score / total_players
            range_score = highest_score - lowest_score

            print(f"Scores processed: {score_list}")
            print(f"Total players: {total_players}")
            print(f"Total score: {total_score}")
            print(f"Average score: {average_score}")
            print(f"High score: {highest_score}")
            print(f"Low score: {lowest_score}")
            print(f"Score range: {range_score}")

        except ValueError:
            print("Error: please provide all number arguments")

        except Exception:
            print("Error: an error occurred within the process !")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py",
            "<score1> <score2> ..."
            )
