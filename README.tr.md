## ML Modelling - Drug Disease Analysis

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/ML-Modelling-Drug-Disease-Analysis/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/ML-Modelling-Drug-Disease-Analysis/blob/main/README.md)

`./dataset`: dizin ***.xlsx*** formatında verisetini içerir. Veriseti sadece 4 tür sınıf içermektedir. Boş değerler doldurulmuş ve Z-score normalizasyon yapılmıştır.

> **Note**: 
> `grid_search.py` hiper parametre taraması yapar, verilen parametre sayısına göre kodun yürütme süresi uzun olabilir. ./results dizini içerisinde; önceden kendi çalıştırmalarımla elde ettiğim grid search sonuçlarına göz atabilirsiniz.



 - Orijinal veri seti [***Mice Protein Expression Data Set***](https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression)

### Veri Kümesi Bilgileri

Veri seti, 77 protein/protein modifikasyonunun ekspresyon seviyelerinden oluşur. Toplam 35 fare için 19 control (normal) ve 16 trizomik fare vardır. Deneylerde, numune/fare başına her protein için 15 ölçüm kaydedildi, protein başına toplam 525 ölçüm vardır 
Sınıflar:  
c-CS-s: öğrenmesi için uyarılmış, saline enjekte edilmiş kontrol fareleri (9 fare)  
c-CS-m: öğrenmesi için uyarılmış, memantine enjekte edilmiş kontrol fareleri (10 fare)  
t-CS-s: öğrenmek için uyarılmış, saline enjekte edilmiş (7 fare)  
t-CS-m: öğrenmek için uyarılmış, memantine enjekte edilmiş (9 fare)  

Amaç, sınıflar arasında ayrım yapan protein alt kümelerini belirlemektir. 
