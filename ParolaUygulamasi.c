#include <stdio.h>
int main(){
	int parola = 1234,hak=3,bp;
	while(hak>0){
		printf("Lutfen parolayi giriniz: \n");
		scanf("%d",&bp);
		if(bp<1000 || bp>9999){
			printf("Lutfen dogru aralikta bir parola giriniz.");
		}
		else{
			if(bp==parola){
				printf("Parola dogru, hos geldiniz.");
				getch();
				break;
			}
			else{
				printf("Yanlis parola, %d hakkiniz kaldi.\n",hak-1);
				hak--;
			}
		}
	}
	return 0;
}
