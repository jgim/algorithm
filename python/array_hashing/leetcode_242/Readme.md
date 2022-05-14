***

### Subject

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


#### Example:

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

#### constraints

```
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
```

***

### result

#### < solution_isAnagram1 >
```
05/14/2022 16:25	Accepted	81 ms	14.4 MB	python3
05/14/2022 16:25	Accepted	65 ms	14.5 MB	python3
05/14/2022 16:24	Accepted	104 ms	14.4 MB	python3
```
- dictionary를 활용
- s 문자열에 값이 dictionary +1을 추가시켜서 넣어줌
- t 문자열을 돌리며 값을 빼줌
- 만약 값이 존재하지 않거나, -가 된다면 false 리턴

#### < solution_isAnagram2 >
```
05/14/2022 16:35	Accepted	71 ms	14.5 MB	python3
05/14/2022 16:35	Accepted	48 ms	14.4 MB	python3
05/14/2022 16:34	Accepted	41 ms	14.4 MB	python3
```
- dictionary 2개를 만들어 s와 t를 각각 넣어줌
- python은 dictionary간 비교가 가능
- 속도는 넣고 빼주는 것보다 더 빠르게 나옴

#### < solution_isAnagram3 >
```
05/14/2022 16:40	Accepted	75 ms	15.2 MB	python3
05/14/2022 16:39	Accepted	90 ms	15.1 MB	python3
05/14/2022 16:39	Accepted	73 ms	15.2 MB	python3
```
- sorted로 문자열을 정리해서 비교
- 공간복잡도와 시간 복잡도 모두 hash 방식보다 많이 걸림

***
