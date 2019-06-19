import re


##过滤HTML中的标签
# 将HTML中标签等信息去掉
# @param htmlstr HTML字符串.
def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile("//<!\[CDATA\[[^>]*//\]\]>", re.I)  #匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s

##替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
# @param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


if __name__ == '__main__':
    print("============remove html from html============")
    re_pat = re.compile(r'<([a-z]+)([^<>]+)*(>(.*)<\/\\1>|\/>)')
    html='''<div data-automation="jobDescription" class="Pdwn1mb"><span class="K1Fdmkw"><div data-automation="desktopTemplate" class="FG9Y_EB"><meta charset="utf-8">
<style type="text/css"><!--#VideoJobAd,.videoembed{display:block;height:310px;padding:5px 0;text-align:center;width:100%}#jobadControl .videoembed{border:1px solid #ccc}.job-template__wrapper{font-size:12px;font-family:Helvetica,Arial,sans-serif;overflow:hidden;background-color:#fff;color:#404040;line-height:normal;box-sizing:content-box;width:460px;max-width:460px}.job-template__wrapper .details,.job-template__wrapper .jobtitle,.job-template__wrapper .subheading,.job-template__wrapper ul.templatebullet,.job-template__wrapper ul.templatebulletnormal{color:#1c1c1c;word-wrap:break-word}.job-template__wrapper .templatetext,.job-template__wrapper ul.templatebulletnormal{font-size:10pt;font-weight:400;word-wrap:break-word}.job-template__wrapper .jobtitle{font-size:20pt;font-weight:700}.job-template__wrapper .subheading{font-size:15pt;font-weight:700}.job-template__wrapper h1{font-size:26px;margin:18px 0;font-weight:400}.job-template__wrapper h2,.job-template__wrapper h3{font-size:14px;margin:18px 0;color:#0d3880;font-weight:700}.job-template__wrapper h3{margin:9px 0}.job-template__wrapper h4{font-size:12px;margin:9px 0}.job-template__wrapper b,.job-template__wrapper strong{font-weight:700}.job-template__wrapper em,.job-template__wrapper i{font-style:italic}.job-template__wrapper blockquote{margin:1em 40px}.job-template__wrapper td{vertical-align:middle}.job-template__wrapper .templatetext h2{font-size:21px;margin:0;color:#1c1c1c}.job-template__wrapper ul.templatebullet{font-size:9pt;font-weight:700}.job-template__wrapper .templatebullet li,.job-template__wrapper .templatebulletnormal li,.job-template__wrapper .templatetext li{list-style-position:outside;list-style:disc;margin-left:14px}.job-template__wrapper .templatetext ol,.job-template__wrapper .templatetext ul{margin-top:8px}.job-template__wrapper .templatetext ol li{list-style-position:outside;list-style:decimal;margin-left:20px}.job-template__wrapper .details{font-size:8pt;font-weight:400;word-wrap:break-word}.job-template__wrapper .tempmargin{margin:0 30px;padding:10px 0}.job-template__wrapper ul.templatebullet{margin:0 0 0 40px;padding:10px 0}.job-template__wrapper small{font-size:11px;font-weight:400;color:#636363}.job-template__wrapper a{text-decoration:none}.job-template__wrapper a:focus{outline:thin dotted}.job-template__wrapper a:active,.job-template__wrapper a:link,.job-template__wrapper a:visited{color:#2765cf}.job-template__wrapper hr{border:none;border-top:1px solid #dadada}.job-template__wrapper dl,.job-template__wrapper menu,.job-template__wrapper ol,.job-template__wrapper p,.job-template__wrapper ul{margin:9px 0}.job-template__wrapper menu,.job-template__wrapper ol,.job-template__wrapper ul,.job-template__wrapper ul li{padding:0}.job-template__wrapper [valign=top]{vertical-align:top}.job-template__wrapper sub,.job-template__wrapper sup{position:relative;vertical-align:baseline;line-height:0;font-size:9px}.job-template__wrapper sup{top:-.5em}.job-template__wrapper sub{bottom:-.25em}.job-template__wrapper .content{margin:0 11px;padding:15px 20px 35px;background:#fff;position:relative;z-index:3;top:4px;min-height:200px;margin-right:0}--></style>
<style type="text/css">
<!--
.job-template__wrapper .tempborder { width: 400px; border: 30px solid #ee3124; text-align: left; font-family: Helvetica, Arial; }
.job-template__wrapper .tempborder .templogo { text-align: center; padding: 30px 0 0; font-size: 0; line-height: 0; ; background: #ee3124 }
.job-template__wrapper .tempborder .tempmargin { margin: 0 20px; padding: 20px 0 20px; }
.job-template__wrapper .tempborder .jobtitle { color: #fff; text-align: center; margin: 0; padding: 0 20px 30px; display: block; background: #ee3124 }
.job-template__wrapper .tempborder .subheading, .job-template__wrapper .tempborder h2 { color: #000!important; text-align: center; margin: 0; padding: 0 0 10px; display: block; font-size: 16px }
.job-template__wrapper .tempborder .templatebullet li { color: #000; text-align: left; margin-left: -25px!important; }
.job-template__wrapper .tempborder .templatetext li { color: #000!important; text-align: left; margin-left: 15px; }
.job-template__wrapper .tempborder .templatetext { color: #000; text-align: left; }
.job-template__wrapper .tempborder .details { color: #000; text-align: center; padding-top: 20px; font-size: 13px; }
.job-template__wrapper .tempborder .temphidden { font-size: 1px; color: #fff }
-->
</style>
<div class="job-template__wrapper">
  <div class="tempborder">
    <h1 class="jobtitle">UX Designer </h1>
    <div class="tempmargin">
      <div class="templatetext">
        <p><strong>Who is EROAD?</strong></p>
        <p>EROAD modernises road charging and compliance for road transport by replacing paper-based systems with easy-to-use electronic systems. EROAD introduced the world's first nationwide electronic road user charging system in New Zealand in 2009. The
          company is headquartered in Auckland, with offices in Portland, Oregon and is listed on the New Zealand Exchange (NZX)</p>
        <p><strong>The Role</strong></p>
        <p>As a Mid - Senior UX Designer you will craft digital experiences that are useful, usable and delightful for the customer, through applying systematic design strategies. You will work closely with our product managers to better understand the problems
          that EROAD’s customers need to solve. Through user research, you will articulate precisely our customers jobs to be done and propose designs that help our customers succeed. </p>
        <p>As a member of the UX team you will be working on a number of campaigns and initiatives for our clients.</p>
        <p> <strong>Duties will include but not limited to: </strong></p>
        <ul>
          <li>Supporting the product managers in the development of product vision by conducting user research and prioritising our customers pain points.</li>
          <li>Use metrics driven design thinking to look at our current user patterns and identify areas for product improvements and potential new offering.</li>
          <li>Understand EROAD’s customers and their needs. Use suitable user research techniques e.g. user interviews, on site observation, surveys and evaluate user feedback.</li>
          <li>Partner with the UX team to develop customer centred user journeys.</li>
          <li>Work with Product Managers and cross functional teams to identify possible design solutions through workshops and collaborative design sessions</li>
          <li>Engage in day-to-day activities with the Engineering Teams. This involves attending daily scrums as required and providing UX direction and education</li>
          <li>Promote user centred design and a consistent UX across all of EROAD product offerings</li>
          <li>Transform complex design challenges into easy-to-use, delightful experiences. Simplicity is key!</li>
        </ul>
        <p><strong>What are we looking for?</strong></p>
        <ul>
          <li>Strong customer focus</li>
          <li>Can do attitude</li>
          <li>Strong attention to detail</li>
          <li>User research experience</li>
          <li>Quantitative research and analysis</li>
          <li>Prototyping and User testing</li>
          <li>4+ years of design experience with a focus in digital.</li>
          <li>Bachelor’s degree in Design, Human-Computer Interaction, Psychology, Information Systems or equivalent experience.</li>
          <li>Previous experience with presentation of ideas and proposals </li>
        </ul>
        <p><strong>Benefits: </strong></p>
        <p>This is an excellent opportunity to take on a pivotal role in one of New Zealand’s fastest growing high-tech companies. EROAD offers a competitive salary and benefits, excellent career development opportunities, and a fun, fast-paced work environment.</p>
        <p>We ensure you have the tools, technology and training to do your best work, and offer flexible work hours to help ensure a healthy work/life balance.</p>
        <p>But don’t take our word for it – see what other EROADers have to say about working here.</p>
        <p>For further details please feel free to call James Blake, Recruitment Manager on 09 9274721.</p>
      </div>
      <div class="details"> </div>
    </div>
    <div class="templogo"><img src="https://seekcdn.com/templates/24084597_1_logo.png" width="103" height="87" alt=""></div>
  </div>
</div></div></span><span class="_2njvnpA _1pia1SL"><div><div data-automation="mobileTemplate" class="_17ZYgCC"><p><strong>Who is EROAD?</strong></p>  <p>EROAD modernises road charging and compliance for road transport by replacing paper-based systems with easy-to-use electronic systems. EROAD introduced the world's first nationwide electronic road user charging system in New Zealand in 2009. The company is headquartered in Auckland, with offices in Portland, Oregon and is listed on the New Zealand Exchange (NZX)</p>  <p><strong>The Role</strong></p>  <p>As a Mid - Senior UX Designer you will craft digital experiences that are useful, usable and delightful for the customer, through applying systematic design strategies. You will work closely with our product managers to better understand the problems that EROAD’s customers need to solve. Through user research, you will articulate precisely our customers jobs to be done and propose designs that help our customers succeed. </p>  <p>As a member of the UX team you will be working on a number of campaigns and initiatives for our clients.</p>  <p> <strong>Duties will include but not limited to: </strong></p> <ul> <li>Supporting the product managers in the development of product vision by conducting user research and prioritising our customers pain points.</li> <li>Use metrics driven design thinking to look at our current user patterns and identify areas for product improvements and potential new offering.</li> <li>Understand EROAD’s customers and their needs. Use suitable user research techniques e.g. user interviews, on site observation, surveys and evaluate user feedback.</li> <li>Partner with the UX team to develop customer centred user journeys.</li> <li>Work with Product Managers and cross functional teams to identify possible design solutions through workshops and collaborative design sessions</li> <li>Engage in day-to-day activities with the Engineering Teams. This involves attending daily scrums as required and providing UX direction and education</li> <li>Promote user centred design and a consistent UX across all of EROAD product offerings</li> <li>Transform complex design challenges into easy-to-use, delightful experiences. Simplicity is key!</li></ul> <p><strong>What are we looking for?</strong></p> <ul> <li>Strong customer focus</li> <li>Can do attitude</li> <li>Strong attention to detail</li> <li>User research experience</li> <li>Quantitative research and analysis</li> <li>Prototyping and User testing</li> <li>4+ years of design experience with a focus in digital.</li> <li>Bachelor’s degree in Design, Human-Computer Interaction, Psychology, Information Systems or equivalent experience.</li> <li>Previous experience with presentation of ideas and proposals </li></ul> <p><strong>Benefits: </strong></p>  <p>This is an excellent opportunity to take on a pivotal role in one of New Zealand’s fastest growing high-tech companies. EROAD offers a competitive salary and benefits, excellent career development opportunities, and a fun, fast-paced work environment.</p>  <p>We ensure you have the tools, technology and training to do your best work, and offer flexible work hours to help ensure a healthy work/life balance.</p>  <p>But don’t take our word for it – see what other EROADers have to say about working here.</p>  <p>For further details please feel free to call James Blake, Recruitment Manager on 09 9274721.</p></div></div></span></div>
    '''

    h ='''<div data-automation="jobDescription" class="Pdwn1mb"><span class=""><div><div data-automation="mobileTemplate" class="_17ZYgCC"><p>Lentune is a rapidly growing software development company based in EPIC Innovation in the Christchurch CBD. Lentune develop smarter business process software with a strong emphasis on accounting automation. Currently our core markets are Wholesalers and Construction companies.</p> <p>As we are quickly growing we are looking for someone with a passion for customer service and an eye for detail to join our sales support team. The role will be dynamic with plenty of scope for creative license to ultimately help springboard our support team into being a market leader. </p> <p>The person chosen for this role would be responsible for the following task.</p> <ul> <li>Learning and familiarising themselves with our software and the technical aspects of it's setup.</li> <li>Help produce/modernise training documentation for new and existing feature.</li> <li>Manage new and existing customer relationships.</li> <li>Run in-house training sessions for new customer.</li> <li>Take support calls.</li> <li>Assist the sales team with onboarding new customers and data manipulation.</li></ul> <p> </p> <p>The ideal candidate would be someone who is</p> <ul> <li>Comfortable around IT systems and is willing to learn new things.</li> <li>Willing to take ownership of a task.</li> <li>Strong problem solving skills and the ability to think on their feet</li> <li>Works well in a team environment</li> <li>Happy to do day travel domestically</li> <li>Willingness to learn new system</li></ul> <p> </p> <p>The candidate would have the following knowledge or education base</p> <ul> <li>Ideally worked in a previous support or account management  role.</li> <li>Have strong verbal and written English skills.</li> <li>Present well to customers</li> <li>Have knowledge of accounting processes</li> <li>Basic knowledge of IT infrastructure</li></ul> <p>The role is full time and can be an immediate start.</p></div></div></span></div>'''
    # result, num = re_pat.subn(' ', html)
    # print('num:{}'.format(num))
    # print('result:{}'.format(result))
    result = filter_tags(h)
    print('result:{}'.format(result))