import os
import nltk
import re
from nltk.tokenize import sent_tokenize
from pyvi import ViTokenizer
import  text_utils_vietnamese
from rouge_vn import pyrouge_vn

# SPECICAL_CHARACTER = {'(', ')', '[', ']', '”', '“', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# QUOTE = {'(', ')', '[', ']', '”', '“', '*'}
#
# a = text_utils_vietnamese.split_sentences("/home/hieupd/PycharmProjects/convert_to_extract/vietnamese/Documents/cluster_192/12380367.body.txt")
#
# for i in a:
#     print(i)
#     print('+++++')

# a = """
#
# lễ khai_mạc đậm màu_sắc dân_gian ( ảnh nhan_sáng ttxvn ) festival_trà_thái nguyênviệt nam lần thứ hai năm 2013 được tổ_chức nhằm tiếp_tục tôn_vinh cây chè , các sản_phẩm và văn_hóa trà , giới_thiệu , quảng_bá hình_ảnh đất_nước con_người việt_nam và tỉnh thái_nguyên nâng cao hơn nữa hiệu_quả sản_xuất kinh_doanh đối_với cây chè và sản_phẩm trà , tiếp_tục khẳng_định thương_hiệu " đệ nhất danh trà " với du_khách trong nước và quốc_tế tăng_cường mối quan_hệ liên_doanh , liên_kết , hợp_tác đầu_tư trên mọi lĩnh_vực , đặc_biệt là phát_triển cây chè , sản_xuất chế_biến và tiêu_thụ sản_phẩm trà với các tỉnh trong cả nước và trên thị_trường quốc_tế
# """
# print(len(a.strip().split()))
#
from text_utils_vietnamese import text_process_vietnamese
a = ['''
Thái Bình
Nông dân tuần hành ở Bangkok đòi chính phủ thanh toán tiền mua gạo. Ảnh Nationmultimedia.com
Hãng tin AP đưa tin từ Bangkok cho biết có hai công nhân bị thương nặng phải vào bệnh viện vì bom nổ khi họ đang sắp xếp các chậu hoa trên dải phân cách một đường phố ở trung tâm Bangkok. Ông Saemdin Lertbutr, phụ trách một nhóm biểu tình, cho hãng AP biết không có người biểu tình nào bị thương và nhận định vụ nổ có thể chỉ nhằm đe dọa vì cường độ của quả bom – cũng có thể là một trái pháo lớn - không đủ gây sát thương hay đe dọa tính mạng.
Từ khi các cuộc biểu tình đòi Thủ tướng Yingluck Shinawatra phải từ chức bùng phát ở Bangkok hồi đầu tháng 11-2013 đến nay đã có gần 10 người thiệt mạng và hàng chục người bị thương vì bạo lực.
Trong một diễn biến liên quan, sáng nay hàng trăm nông dân Thái Lan đã tổ chức tuần hành bên ngoài trụ sở Bộ Tư pháp nước này để phản đối việc chính phủ chậm thanh toán cho họ tiền mua lúa gạo theo một chương trình trợ giá lúa gạo gây nhiều tranh cãi.
Các nông dân cho hãng tin Reuters biết, trong chiều nay thứ Hai 10-2 họ sẽ tiếp tục tuần hành tới một doanh trại quân đội ở phía Bắc Bangkok, nơi Thủ tướng tạm quyền Yingluck Shinawatra đặt văn phòng làm việc từ tháng 1-2014, do các cuộc biểu tình chống chính phủ làm gián đoạn hoạt động thường nhật của các cơ quan công quyền ở trung tâm thủ đô.
Chương trình mua lúa gạo của nông dân với giá cao hơn thị trường là một chính sách mang dấu ấn (signature policy) của Thủ tướng Yingluck – người giành thắng lợi trong cuộc tổng tuyển cử năm 2011 nhờ lá phiếu của hàng triệu nông dân ở miền Bắc Thái Lan. Tuy nhiên, chương trình bị phe đối lập coi là đầy tham nhũng và lãng phí; và đây cũng là một trong những nguyên nhân chính thúc đẩy giới trung lưu đô thị xuống đường đòi bà Yingluck phải từ chức.
Chính phủ hiện hành ở Thái Lan là chính phủ tạm quyền và không có đủ quyền lực để lấy tiền từ ngân sách quốc gia thanh toán cho việc mua gạo của nông dân theo giá cam kết, nhiều nông dân đã phải chờ đợi rất nhiều tháng vẫn chưa nhận được tiền.
Cho đến nay, nông dân vẫn là lực lượng chính ủng hộ bà Yingluck và trong cuộc đối đầu giữa chính phủ với phe đối lập hiện nay, nông dân đứng ngoài các cuộc biểu tình.
Để lôi kéo nông dân tham gia, sáng nay thủ lĩnh phe đối lập Suthep Thaugsuban đã dẫn đầu một cuộc tuần hành từ trung tâm Bangkok đến các khu dân cư thượng lưu Thonglor và Ekkamai để quyên góp tiền bạc cho nông dân. “Chúng tôi sẽ gây quỹ cho những người nông dân này. Họ cần có tiền để khởi kiện chính phủ”, ông Suthep nói.

''']
a = text_process_vietnamese(a)[0]

b = text_process_vietnamese([ '(TBKTSG Online) - Bom nổ gần một địa điểm biểu tình chống chính phủ Thái Lan trưa nay thứ Hai 10-2 làm sáu công nhân vệ sinh bị thương, trong khi hàng trăm nông dân cũng tổ chức tuần hành đòi chính phủ tạm quyền phải thanh toán tiền mua gạo.'])
print(pyrouge_vn.rouge_1(a,b, 0))
