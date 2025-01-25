func mergeAlternately(word1 string, word2 string) string {
	merged_word := ""
	i := 0
	j:= 0

	for i < len(word1) && j < len(word2) {
		merged_word += string(word1[i])
		merged_word += string(word2[j])
		i++
		j++
	}

	for i < len(word1) {
		merged_word += string(word1[i])
        i++
	}
	for j < len(word2) {
		merged_word += string(word2[j])
        j++
	}

	fmt.Println(i, j, merged_word)
    return merged_word
}