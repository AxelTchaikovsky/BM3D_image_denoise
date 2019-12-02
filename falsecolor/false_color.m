clc;
clear;
close all;
srcImg=imread('1.jpg');
srcImg=rgb2gray(srcImg);
img=srcImg;
subplot(231),imshow(srcImg),title('original');
%I=double(I); 
[M,N]=size(srcImg);

R=zeros(M,N);
G=zeros(M,N);
B=zeros(M,N);         
trans = zeros(M,N);
for i=1:M
    for j=1:N
        %RED
        if srcImg(i,j)>5 && srcImg(i,j)<=45
            R(i,j)=5*(srcImg(i,j)-5);
        end
        if (srcImg(i,j)>45 && srcImg(i,j)<=65)||(srcImg(i,j)>175 && srcImg(i,j)<=195)
            R(i,j)=200;
        end
        if srcImg(i,j)>65 && srcImg(i,j)<=105
            R(i,j)=5*(105-srcImg(i,j));
        end
        if srcImg(i,j)>135 && srcImg(i,j)<=175
            R(i,j)=5*(srcImg(i,j)-135);
        end
        if srcImg(i,j)>195 && srcImg(i,j)<=235
            R(i,j)=5*(235-srcImg(i,j));
        end
        %GREEN
        if srcImg(i,j)>20 && srcImg(i,j)<=80
            G(i,j)=4*(srcImg(i,j)-20);
        end
        if srcImg(i,j)>80 && srcImg(i,j)<=110
            G(i,j)=200;
        end
        if srcImg(i,j)>110 && srcImg(i,j)<=170
            G(i,j)=4*(170-srcImg(i,j));
        end
        %BLUE
        if srcImg(i,j)>0 && srcImg(i,j)<=60
            B(i,j)=180-6*abs(srcImg(i,j)-30);
        end
        if srcImg(i,j)>60 && srcImg(i,j)<=120
            B(i,j)=180-6*abs(srcImg(i,j)-90);
        end
        if srcImg(i,j)>120 && srcImg(i,j)<=180
            B(i,j)=180-6*abs(srcImg(i,j)-150);
        end
        if srcImg(i,j)>180 && srcImg(i,j)<=240
            B(i,j)=180-6*abs(srcImg(i,j)-210);
        end
    end
end

R=uint8(R);
G=uint8(G);
B=uint8(B);
subplot(232),imshow(cat(3,R,trans,trans)),title('red');
subplot(233),imshow(cat(3,trans,G,trans)),title('green');
subplot(234),imshow(cat(3,trans,trans,B)),title('blue');
img_new=cat(3,R,G,B);    %ºÏ³ÉRGBÍ¼Ïñ
subplot(235),imshow(img_new),title('result');