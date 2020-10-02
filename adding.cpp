#include<iostream>

using namespace std;

class MTStack{

};

class FullStack{

};

class DStack{

    private:
        int arr[200];
        int topSmall;
        int topLarge;
    
    public:
        //In the constructor, initialze the top of small stack as 0 and large stack as 199 (right extreme)
        //The small stack grows towards the right and the large stack grows towards the left.
        DStack(){
            topSmall = -1;
            topLarge = 200;
        }

        void push(int x){
            if(x>1000){

                try{
                // topLarge -1  will be the new top after inserting number, so check if topSmall does not coincide with new topLarge
                if(topLarge - 1 > topSmall){
                    topLarge--;
                    arr[topLarge] = x;
                    
                }
                else{
                    throw (FullStack());
                }
            }
            catch (FullStack f){
                cout<<"caught exception of FullStack class."<<endl;
            }
            }
            else{
                try{
                if(topSmall + 1 < topLarge){
                    topSmall++;
                    arr[topSmall] = x;
                    
                }
                else{
                    throw (FullStack());
                }
            }
            catch (FullStack f){
                cout<<"Caught exception of FullStack class."<<endl;
            }
            }
        }

        int popSmall(){

            try{
            if(topSmall != -1){
                int t = arr[topSmall];
                topSmall--;
                
            }
            else{
                throw (MTStack());
            }
        }
            catch(MTStack m){
                cout<<"Caught exception of MTStack class"<<endl;
            }
        }

        void popLarge(){

            try{
            if(topLarge != 200){
                int t = arr[topLarge];
                topLarge++;
                
            }
            else{
                throw (MTStack());
            }
        }
            catch(MTStack m){
                cout<<"Caught exception of MTStack class"<<endl;
            }
        }

        int getTopSmall(){
            if(topSmall == -1){
                return -1;
            }
            else{
                return arr[topSmall];
            }
        }

        int getTopLarge(){
            if(topLarge == 200){
                return -1;
            }
            else{
                return arr[topLarge];
            }
        }

        int sizeSmall(){
            return topSmall + 1;
        }

        int sizeLarge(){
            return 200 - topLarge;
        }

        int size(){
            return sizeSmall() + sizeLarge();
        }

        bool isFull(){
            return topSmall + 1 == topLarge;
        }

        // give parameter 's' for only small stack, 'l' for only large stack and 'b' for both stacks.
        void print(char c){
            
            if(c == 's'){
                cout<<"The small stack is -"<<endl;
                for(int i=0;i<=topSmall;i++) cout<<arr[i]<<" ";
                cout<<"\n";
            }
            else if(c == 'l'){
                cout<<"The large stack is -"<<endl;
                for(int i=199;i>=topLarge;i--){
                    cout<<arr[i]<<" ";
                }
                cout<<"\n";
            }
            else if(c == 'b'){
                cout<<"The small stack is -"<<endl;
                for(int i=0;i<=topSmall;i++) cout<<arr[i]<<" ";
                cout<<"\n";
                cout<<"The large stack is -"<<endl;
                for(int i=199;i>=topLarge;i--){
                    cout<<arr[i]<<" ";
            }
            cout<<"\n";
        }
    }

};

int main(){
    
    DStack ds;

    ds.push(100);
    ds.push(1001);
    ds.push(10);
    ds.push(10000);
    cout<<ds.size()<<endl;
    cout<<ds.getTopLarge()<<endl;
    cout<<ds.getTopSmall()<<endl;

    cout<<ds.sizeSmall()<<" "<<ds.sizeLarge()<<endl;
    
    ds.print('s');
    ds.print('l');
    ds.print('b');

    cout<<ds.isFull()<<endl;

    ds.popSmall();
    ds.popSmall();
    ds.popSmall();

    for(int i=0;i<200;i++){
        ds.push(i);
    }
    
    return 0;
}
