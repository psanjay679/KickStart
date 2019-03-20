def main():

	t = int(input())
	for i in range(t):
		n = int(input())
		ar, br = dict(), dict()

		for j in range(n):
			a, b = map(str, input().split())

			ar[a] = 1
			br[b] = 1

		ans = 'Yes'

		for a in ar:
			if a in br:
				ans = 'No'
				del ar[a]
				del br[a]
				break
		for a in ar:
			if a in br:
				ans = 'No'
				del ar[a]
				del br[a]
				break
		else:
			ans = 'Yes'

		print('Case #{tc_no}: {ans}'.format(tc_no=i + 1, ans=ans))

if __name__ == '__main__':
	main()