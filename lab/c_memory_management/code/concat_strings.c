#include <stdio.h>

void concat_strings(char *str1, const char *str2) {
  char *str1_ptr = str1;
  // Find null character of str1
  while (*str1 != '\0') {
    str1++;
  }

  while (*str2 != '\0') {
    *str1 = *str2;
    str1++;
    str2++;
  }

  *str1 = '\0';
  printf("%s", str1_ptr);
}

int main() {
  char str1[100] = "Hello ";
  const char *str2 = "World";
  concat_strings(str1, str2);
  return 0;
}
