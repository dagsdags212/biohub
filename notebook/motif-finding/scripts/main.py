class KmerComposition:
    def __init__(self, text: str, k: int) -> None:
        self.text = text
        self.k = k

    def frequency_table(self) -> dict[str, int]:
        """Returns a frequency table containing all k-mer counts."""
        kmer_counts = {}
        for i in range(len(self.text)-self.k+1):
            kmer = self.text[i:i+self.k]
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1
        # Return all k-mers sorted by count
        return kmer_counts

    def most_frequent_kmer(self) -> tuple[int, list[str]]:
        """Returns the most frequent k-mer and its counts from a frequency table. 
        If there are multiple most-frequent k-mers, return them in a list."""
        freq_map = self.frequency_table()
        max_count = max(freq_map.values())
        most_freq_kmers = []
        for kmer, count in freq_map.items():
            if count == max_count:
                most_freq_kmers.append(kmer)
        return (max_count, most_freq_kmers)

def pattern_count(text: str, pattern: str) -> int:
  """Counts the number of times `pattern` occurs as a substring of `text`."""
  count: int = 0
  k = len(pattern)
  for i in range(len(text)-k+1):
    if text[i:i+k] == pattern:
      count += 1
  return count
