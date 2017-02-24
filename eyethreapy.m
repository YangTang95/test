%eye threapy
function eyethreapy
close all;clc;clear all;
n=input('therapy type');
k=input('rounds');
switch n
    case 'pur'
       
        for j=1:k
            for i=1:512
    
                t = linspace(0,2*pi,100);
                x = cos(t)+i/4; 
                y = sin(t)+1; 
                fill(x,y,'r');
                axis equal;
                xlim([0,128]);
                ylim([0,3]);
                pause(0.01); %speed
            
            end
            
            for i=1:512
    
                t = linspace(0,2*pi,100);
                x = cos(t)+128-i/4; 
                y = sin(t)+1; 
                fill(x,y,'r');
                axis equal;
                xlim([0,128]);
                ylim([0,3]);
                pause(0.01);            
            end   
        end
        
    case 'sac'
        
        for j=1:k
            for i=1:25.6    
                t = linspace(0,2*pi,100);
                x = cos(t)+10*i; 
                y = sin(t)+1; 
                fill(x,y,'r');
                axis equal;
                xlim([0,256]);
                ylim([0,3]);
                pause(1);
            end
            
            for i=1:25.6    
                t = linspace(0,2*pi,100);
                x = cos(t)+256-10*i; 
                y = sin(t)+1; 
                fill(x,y,'r');
                axis equal;
                xlim([0,256]);
                ylim([0,3]);
                pause(1);           
            end            
        end
        
    case 'udpur'
       
        for j=1:k
            for i=1:512
    
                t = linspace(0,2*pi,100);
                x = cos(t)+1;
                y = sin(t)+i/4;  
                fill(x,y,'r');
                axis equal;
                ylim([0,128]);
                xlim([0,3]);
                pause(0.01); %speed
            
            end
            
            for i=1:512
    
                t = linspace(0,2*pi,100);
                x = cos(t)+1;
                y = sin(t)+128-i/4; 
                fill(x,y,'r');
                axis equal;
                ylim([0,128]);
                xlim([0,3]);
                pause(0.01);            
            end
   
        end
    case 'udsac'
        
        for j=1:k
            for i=1:25.6
    
                t = linspace(0,2*pi,100);
                x = cos(t) +1;
                y = sin(t) +10*i;
                fill(x,y,'r');
                axis equal;
                ylim([0,256]);
                xlim([0,3]);
                pause(1);
            end
            
            for i=1:25.6
    
                t = linspace(0,2*pi,100);
                x = cos(t)+ 1;
                y = sin(t)+ 256-10*i;
                fill(x,y,'r');
                axis equal;
                ylim([0,256]);
                xlim([0,3]);
                pause(1);
           
            end
            
        end
end
end