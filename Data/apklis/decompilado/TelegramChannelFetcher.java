package com.ermetic.circuitoshabana.data;

import android.util.Log;
import androidx.compose.ui.tooling.preview.AndroidUiModes;
import com.ermetic.circuitoshabana.service.AlarmaCircuito;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.Date;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.NoSuchElementException;
import java.util.TimeZone;
import kotlin.Metadata;
import kotlin.ResultKt;
import kotlin.Unit;
import kotlin.collections.CollectionsKt;
import kotlin.comparisons.ComparisonsKt;
import kotlin.coroutines.Continuation;
import kotlin.coroutines.intrinsics.IntrinsicsKt;
import kotlin.coroutines.jvm.internal.Boxing;
import kotlin.coroutines.jvm.internal.DebugMetadata;
import kotlin.coroutines.jvm.internal.SuspendLambda;
import kotlin.jvm.functions.Function2;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.StringsKt;
import kotlinx.coroutines.BuildersKt;
import kotlinx.coroutines.CoroutineScope;
import kotlinx.coroutines.Dispatchers;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

/* JADX INFO: compiled from: TelegramChannelFetcher.kt */
/* JADX INFO: loaded from: classes2.dex */
@Metadata(d1 = {"\u0000N\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0003\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\t\n\u0002\b\u0003\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\bÇ\u0002\u0018\u00002\u00020\u0001B\t\b\u0002¢\u0006\u0004\b\u0002\u0010\u0003J\u0010\u0010\t\u001a\u00020\b2\u0006\u0010\n\u001a\u00020\u0005H\u0002J\u0014\u0010\u000b\u001a\b\u0012\u0004\u0012\u00020\r0\fH\u0086@¢\u0006\u0002\u0010\u000eJ\u0010\u0010\u000f\u001a\u00020\u00102\u0006\u0010\u0011\u001a\u00020\u0005H\u0002J\u0016\u0010\u0014\u001a\b\u0012\u0004\u0012\u00020\u00150\f2\u0006\u0010\u0016\u001a\u00020\u0005H\u0002J*\u0010\u0017\u001a\u00020\u00182\u0006\u0010\u0019\u001a\u00020\b2\b\b\u0002\u0010\u001a\u001a\u00020\u001b2\b\b\u0002\u0010\u001c\u001a\u00020\bH\u0086@¢\u0006\u0002\u0010\u001dJ\u0014\u0010\u001e\u001a\b\u0012\u0004\u0012\u00020\u001f0\fH\u0086@¢\u0006\u0002\u0010\u000eR\u000e\u0010\u0004\u001a\u00020\u0005X\u0082T¢\u0006\u0002\n\u0000R\u000e\u0010\u0006\u001a\u00020\u0005X\u0082T¢\u0006\u0002\n\u0000R\u000e\u0010\u0007\u001a\u00020\bX\u0082T¢\u0006\u0002\n\u0000R\u000e\u0010\u0012\u001a\u00020\u0005X\u0082T¢\u0006\u0002\n\u0000R\u000e\u0010\u0013\u001a\u00020\bX\u0082T¢\u0006\u0002\n\u0000¨\u0006 "}, d2 = {"Lcom/ermetic/circuitoshabana/data/TelegramChannelFetcher;", "", "<init>", "()V", "TELEGRAM_CHANNEL_URL", "", "TAG", "OFFSET_HORARIO_VERANO_MS", "", "parsearIsoDateTime", "datetimeStr", "obtenerUltimosReportes", "", "Lcom/ermetic/circuitoshabana/data/ReporteAfectaciones;", "(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "esMensajeRelevante", "", AlarmaCircuito.EXTRA_TEXTO, "UA", "OCHO_DIAS_MS", "descargarPagina", "Lcom/ermetic/circuitoshabana/data/TelegramMensajeRaw;", "url", "sincronizarIncremental", "Lcom/ermetic/circuitoshabana/data/ResultadoSincronizacion;", "ultimoIdConocido", "maxPaginas", "", "ahoraMs", "(JIJLkotlin/coroutines/Continuation;)Ljava/lang/Object;", "obtenerUltimosComunicados", "Lcom/ermetic/circuitoshabana/data/ComunicadoModel;", "app"}, k = 1, mv = {2, 2, 0}, xi = AndroidUiModes.UI_MODE_NIGHT_MASK)
public final class TelegramChannelFetcher {
    public static final int $stable = 0;
    public static final TelegramChannelFetcher INSTANCE = new TelegramChannelFetcher();
    private static final long OCHO_DIAS_MS = 691200000;
    private static final long OFFSET_HORARIO_VERANO_MS = 3600000;
    private static final String TAG = "TelegramFetcher";
    private static final String TELEGRAM_CHANNEL_URL = "https://t.me/s/EmpresaElectricaDeLaHabana";
    private static final String UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36";

    private TelegramChannelFetcher() {
    }

    /* JADX INFO: Access modifiers changed from: private */
    public final long parsearIsoDateTime(String datetimeStr) {
        if (StringsKt.isBlank(datetimeStr)) {
            return System.currentTimeMillis();
        }
        try {
            String strTake = StringsKt.take(datetimeStr, 19);
            SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss", Locale.US);
            simpleDateFormat.setTimeZone(TimeZone.getTimeZone("UTC"));
            Date date = simpleDateFormat.parse(strTake);
            return (date != null ? date.getTime() : System.currentTimeMillis()) + 3600000;
        } catch (Exception unused) {
            return System.currentTimeMillis();
        }
    }

    /* JADX INFO: renamed from: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosReportes$2, reason: invalid class name and case insensitive filesystem */
    /* JADX INFO: compiled from: TelegramChannelFetcher.kt */
    @Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0010!\n\u0002\u0018\u0002\n\u0002\u0018\u0002\u0010\u0000\u001a\b\u0012\u0004\u0012\u00020\u00020\u0001*\u00020\u0003H\n"}, d2 = {"<anonymous>", "", "Lcom/ermetic/circuitoshabana/data/ReporteAfectaciones;", "Lkotlinx/coroutines/CoroutineScope;"}, k = 3, mv = {2, 2, 0}, xi = AndroidUiModes.UI_MODE_NIGHT_MASK)
    @DebugMetadata(c = "com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosReportes$2", f = "TelegramChannelFetcher.kt", i = {}, l = {}, m = "invokeSuspend", n = {}, s = {})
    static final class C03372 extends SuspendLambda implements Function2<CoroutineScope, Continuation<? super List<ReporteAfectaciones>>, Object> {
        int label;

        C03372(Continuation<? super C03372> continuation) {
            super(2, continuation);
        }

        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Continuation<Unit> create(Object obj, Continuation<?> continuation) {
            return new C03372(continuation);
        }

        @Override // kotlin.jvm.functions.Function2
        public final Object invoke(CoroutineScope coroutineScope, Continuation<? super List<ReporteAfectaciones>> continuation) {
            return ((C03372) create(coroutineScope, continuation)).invokeSuspend(Unit.INSTANCE);
        }

        /* JADX WARN: Code duplicated, block: B:44:0x0195 A[Catch: Exception -> 0x01e9, TryCatch #1 {Exception -> 0x01e9, blocks: (B:41:0x0187, B:42:0x018f, B:44:0x0195, B:46:0x01a7, B:48:0x01c1, B:50:0x01cd, B:52:0x01d9, B:54:0x01e5, B:38:0x015f, B:10:0x002d, B:12:0x0059, B:15:0x006d, B:17:0x0078, B:19:0x009b, B:22:0x00c3, B:24:0x00d0, B:27:0x00d9, B:29:0x00eb, B:31:0x0109, B:32:0x011b, B:33:0x0128, B:35:0x0142), top: B:61:0x002d, inners: #0 }] */
        /* JADX WARN: Code duplicated, block: B:73:0x01a7 A[SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:79:0x018f A[SYNTHETIC] */
        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Object invokeSuspend(Object obj) {
            int i;
            String texto;
            ReporteAfectaciones reporteAfectaciones;
            String str;
            String str2;
            Elements elements;
            boolean z;
            String strAttr;
            String str3 = "/";
            String str4 = "get(...)";
            IntrinsicsKt.getCOROUTINE_SUSPENDED();
            if (this.label != 0) {
                throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");
            }
            ResultKt.throwOnFailure(obj);
            ArrayList arrayList = new ArrayList();
            ArrayList arrayList2 = new ArrayList();
            String str5 = TelegramChannelFetcher.TELEGRAM_CHANNEL_URL;
            boolean z2 = true;
            int i2 = 1;
            int size = 0;
            while (true) {
                if (i2 < 16 && size < 300) {
                    try {
                        try {
                            Document document = Jsoup.connect(str5).userAgent(TelegramChannelFetcher.UA).timeout(10000).followRedirects(z2).get();
                            Intrinsics.checkNotNullExpressionValue(document, str4);
                            Elements elementsSelect = document.select("div.tgme_widget_message");
                            Intrinsics.checkNotNullExpressionValue(elementsSelect, "select(...)");
                            if (!elementsSelect.isEmpty()) {
                                ArrayList arrayList3 = new ArrayList();
                                int size2 = elementsSelect.size();
                                String str6 = "";
                                int i3 = 0;
                                while (i3 < size2) {
                                    Element element = elementsSelect.get(i3);
                                    Intrinsics.checkNotNullExpressionValue(element, str4);
                                    Element element2 = element;
                                    if (i3 == 0) {
                                        String strAttr2 = element2.attr("data-post");
                                        Intrinsics.checkNotNullExpressionValue(strAttr2, "attr(...)");
                                        str = str3;
                                        str2 = str4;
                                        elements = elementsSelect;
                                        if (StringsKt.contains$default((CharSequence) strAttr2, (CharSequence) str, false, 2, (Object) null)) {
                                            z = true;
                                            str6 = (String) CollectionsKt.last(StringsKt.split$default((CharSequence) strAttr2, new String[]{str}, false, 0, 6, (Object) null));
                                        } else {
                                            z = true;
                                        }
                                    } else {
                                        str = str3;
                                        str2 = str4;
                                        elements = elementsSelect;
                                        z = z2;
                                    }
                                    Element elementFirst = element2.select("time.time, time").first();
                                    if (elementFirst == null || (strAttr = elementFirst.attr("datetime")) == null) {
                                        strAttr = "";
                                    }
                                    long j = TelegramChannelFetcher.INSTANCE.parsearIsoDateTime(strAttr);
                                    Element elementFirst2 = element2.select("div.tgme_widget_message_text, .js-message_text").first();
                                    if (elementFirst2 != null) {
                                        elementFirst2.select("br").before("\n");
                                        String strText = elementFirst2.text();
                                        Intrinsics.checkNotNullExpressionValue(strText, "text(...)");
                                        if (!StringsKt.isBlank(strText)) {
                                            arrayList3.add(new TelegramMensajeRaw(strText, j, 0L, 4, null));
                                        }
                                    }
                                    i3++;
                                    z2 = z;
                                    str3 = str;
                                    str4 = str2;
                                    elementsSelect = elements;
                                }
                                String str7 = str3;
                                String str8 = str4;
                                boolean z3 = z2;
                                arrayList2.addAll(0, arrayList3);
                                size += arrayList3.size();
                                if (str6.length() > 0) {
                                    str5 = "https://t.me/s/EmpresaElectricaDeLaHabana?before=" + str6;
                                    i2++;
                                    z2 = z3;
                                    str3 = str7;
                                    str4 = str8;
                                } else {
                                    i = 300;
                                    for (TelegramMensajeRaw telegramMensajeRaw : CollectionsKt.takeLast(arrayList2, i)) {
                                        texto = telegramMensajeRaw.getTexto();
                                        if (TelegramChannelFetcher.INSTANCE.esMensajeRelevante(texto)) {
                                            reporteAfectaciones = AfectacionesParser.parsearMensajeTelegram$default(AfectacionesParser.INSTANCE, texto, telegramMensajeRaw.getFechaPublicacionMs(), 0L, 4, null);
                                            if (reporteAfectaciones.getCircuitosAfectados().isEmpty() || !reporteAfectaciones.getBloquesAfectados().isEmpty() || !reporteAfectaciones.getCircuitosNormales().isEmpty() || !reporteAfectaciones.getEventosOrdenados().isEmpty()) {
                                                arrayList.add(reporteAfectaciones);
                                            }
                                        }
                                    }
                                    return arrayList;
                                }
                            }
                        } catch (Exception e) {
                            Log.w(TelegramChannelFetcher.TAG, "Lote " + i2 + " falló: " + e.getMessage());
                        }
                    } catch (Exception e2) {
                        Log.e(TelegramChannelFetcher.TAG, "Error durante la recopilación masiva: " + e2.getMessage());
                    }
                }
                i = 300;
                while (r0.hasNext()) {
                    texto = telegramMensajeRaw.getTexto();
                    if (TelegramChannelFetcher.INSTANCE.esMensajeRelevante(texto)) {
                        reporteAfectaciones = AfectacionesParser.parsearMensajeTelegram$default(AfectacionesParser.INSTANCE, texto, telegramMensajeRaw.getFechaPublicacionMs(), 0L, 4, null);
                        if (reporteAfectaciones.getCircuitosAfectados().isEmpty()) {
                        }
                        arrayList.add(reporteAfectaciones);
                    }
                }
                return arrayList;
            }
        }
    }

    public final Object obtenerUltimosReportes(Continuation<? super List<ReporteAfectaciones>> continuation) {
        return BuildersKt.withContext(Dispatchers.getIO(), new C03372(null), continuation);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public final boolean esMensajeRelevante(String texto) {
        String lowerCase = texto.toLowerCase(Locale.ROOT);
        Intrinsics.checkNotNullExpressionValue(lowerCase, "toLowerCase(...)");
        if (!AfectacionesParser.INSTANCE.extraerCircuitos(texto).isEmpty()) {
            return true;
        }
        String str = lowerCase;
        return StringsKt.contains$default((CharSequence) str, (CharSequence) "afectaci", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) AlarmaCircuito.EXTRA_AFECTADO, false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "afectados", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "déficit", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "deficit", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "avería", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "averia", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "disparo", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "restablecido", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "restablecer", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "restableció", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "restablecio", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "servicio", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "energizado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "incorporado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "normalizado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "cerrado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "abierto", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "desconectado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "rotación", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "rotacion", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "interrupción", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "interrupcion", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "apagón", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "apagon", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) str, (CharSequence) "apagado", false, 2, (Object) null) || Traspasos.INSTANCE.contieneIndicios(texto);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public final List<TelegramMensajeRaw> descargarPagina(String url) throws IOException {
        String strAttr;
        Document document = Jsoup.connect(url).userAgent(UA).timeout(10000).followRedirects(true).get();
        Intrinsics.checkNotNullExpressionValue(document, "get(...)");
        ArrayList arrayList = new ArrayList();
        Iterator<Element> it = document.select("div.tgme_widget_message").iterator();
        Intrinsics.checkNotNullExpressionValue(it, "iterator(...)");
        while (it.hasNext()) {
            Element next = it.next();
            Intrinsics.checkNotNullExpressionValue(next, "next(...)");
            Element element = next;
            String strAttr2 = element.attr("data-post");
            Intrinsics.checkNotNullExpressionValue(strAttr2, "attr(...)");
            String str = "";
            Long longOrNull = StringsKt.toLongOrNull(StringsKt.substringAfterLast(strAttr2, '/', ""));
            if (longOrNull != null) {
                long jLongValue = longOrNull.longValue();
                Element elementFirst = element.select("time.time, time").first();
                if (elementFirst != null && (strAttr = elementFirst.attr("datetime")) != null) {
                    str = strAttr;
                }
                long j = parsearIsoDateTime(str);
                Element elementFirst2 = element.select("div.tgme_widget_message_text, .js-message_text").first();
                if (elementFirst2 != null) {
                    elementFirst2.select("br").before("\n");
                    String strText = elementFirst2.text();
                    Intrinsics.checkNotNullExpressionValue(strText, "text(...)");
                    if (!StringsKt.isBlank(strText)) {
                        arrayList.add(new TelegramMensajeRaw(strText, j, jLongValue));
                    }
                }
            }
        }
        return CollectionsKt.sortedWith(arrayList, new Comparator() { // from class: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$descargarPagina$$inlined$sortedBy$1
            /* JADX WARN: Multi-variable type inference failed */
            @Override // java.util.Comparator
            public final int compare(T t, T t2) {
                return ComparisonsKt.compareValues(Long.valueOf(((TelegramMensajeRaw) t).getId()), Long.valueOf(((TelegramMensajeRaw) t2).getId()));
            }
        });
    }

    /* JADX INFO: renamed from: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$sincronizarIncremental$2, reason: invalid class name and case insensitive filesystem */
    /* JADX INFO: compiled from: TelegramChannelFetcher.kt */
    @Metadata(d1 = {"\u0000\n\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\u0010\u0000\u001a\u00020\u0001*\u00020\u0002H\n"}, d2 = {"<anonymous>", "Lcom/ermetic/circuitoshabana/data/ResultadoSincronizacion;", "Lkotlinx/coroutines/CoroutineScope;"}, k = 3, mv = {2, 2, 0}, xi = AndroidUiModes.UI_MODE_NIGHT_MASK)
    @DebugMetadata(c = "com.ermetic.circuitoshabana.data.TelegramChannelFetcher$sincronizarIncremental$2", f = "TelegramChannelFetcher.kt", i = {}, l = {}, m = "invokeSuspend", n = {}, s = {})
    static final class C03382 extends SuspendLambda implements Function2<CoroutineScope, Continuation<? super ResultadoSincronizacion>, Object> {
        final /* synthetic */ long $ahoraMs;
        final /* synthetic */ int $maxPaginas;
        final /* synthetic */ long $ultimoIdConocido;
        int label;

        /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
        C03382(int i, long j, long j2, Continuation<? super C03382> continuation) {
            super(2, continuation);
            this.$maxPaginas = i;
            this.$ultimoIdConocido = j;
            this.$ahoraMs = j2;
        }

        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Continuation<Unit> create(Object obj, Continuation<?> continuation) {
            return new C03382(this.$maxPaginas, this.$ultimoIdConocido, this.$ahoraMs, continuation);
        }

        @Override // kotlin.jvm.functions.Function2
        public final Object invoke(CoroutineScope coroutineScope, Continuation<? super ResultadoSincronizacion> continuation) {
            return ((C03382) create(coroutineScope, continuation)).invokeSuspend(Unit.INSTANCE);
        }

        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Object invokeSuspend(Object obj) {
            long j;
            boolean z;
            boolean z2;
            boolean z3;
            IntrinsicsKt.getCOROUTINE_SUSPENDED();
            if (this.label != 0) {
                throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");
            }
            ResultKt.throwOnFailure(obj);
            LinkedHashMap linkedHashMap = new LinkedHashMap();
            long j2 = 0;
            boolean z4 = false;
            try {
                String str = TelegramChannelFetcher.TELEGRAM_CHANNEL_URL;
                if (1 <= this.$maxPaginas) {
                    z = false;
                    int i = 1;
                    while (true) {
                        try {
                            List<TelegramMensajeRaw> listDescargarPagina = TelegramChannelFetcher.INSTANCE.descargarPagina(str);
                            if (i == 1) {
                                z = true;
                            }
                            try {
                                if (!listDescargarPagina.isEmpty()) {
                                    for (TelegramMensajeRaw telegramMensajeRaw : listDescargarPagina) {
                                        linkedHashMap.put(Boxing.boxLong(telegramMensajeRaw.getId()), telegramMensajeRaw);
                                    }
                                    long id = ((TelegramMensajeRaw) CollectionsKt.first(listDescargarPagina)).getId();
                                    Iterator it = listDescargarPagina.iterator();
                                    if (!it.hasNext()) {
                                        throw new NoSuchElementException();
                                    }
                                    long fechaPublicacionMs = ((TelegramMensajeRaw) it.next()).getFechaPublicacionMs();
                                    while (it.hasNext()) {
                                        long fechaPublicacionMs2 = ((TelegramMensajeRaw) it.next()).getFechaPublicacionMs();
                                        if (fechaPublicacionMs > fechaPublicacionMs2) {
                                            fechaPublicacionMs = fechaPublicacionMs2;
                                        }
                                    }
                                    long j3 = this.$ultimoIdConocido;
                                    if (j3 <= j2 || id > j3 + 1) {
                                        j = j2;
                                        try {
                                            if (fechaPublicacionMs < this.$ahoraMs - TelegramChannelFetcher.OCHO_DIAS_MS) {
                                                break;
                                            }
                                            if (i == this.$maxPaginas) {
                                                if (j3 <= j) {
                                                    break;
                                                }
                                                z4 = true;
                                                break;
                                            }
                                            str = "https://t.me/s/EmpresaElectricaDeLaHabana?before=" + id;
                                            if (i == this.$maxPaginas) {
                                                break;
                                            }
                                            i++;
                                            j2 = j;
                                        } catch (Exception e) {
                                            e = e;
                                        }
                                    }
                                }
                                j = j2;
                                break;
                            } catch (Exception e2) {
                                e = e2;
                                j = j2;
                                Log.e(TelegramChannelFetcher.TAG, "Error en sincronización incremental: " + e.getMessage());
                            }
                        } catch (Exception e3) {
                            j = j2;
                            Log.w(TelegramChannelFetcher.TAG, "Página " + i + " falló: " + e3.getMessage());
                            if (i == 1) {
                                return new ResultadoSincronizacion(CollectionsKt.emptyList(), this.$ultimoIdConocido, false, false);
                            }
                            z3 = true;
                        }
                    }
                    z3 = z4;
                    z2 = z;
                } else {
                    j = 0;
                    z3 = false;
                    z2 = false;
                }
            } catch (Exception e4) {
                e = e4;
                j = 0;
                z = false;
            }
            Collection collectionValues = linkedHashMap.values();
            long j4 = this.$ultimoIdConocido;
            ArrayList arrayList = new ArrayList();
            for (Object obj2 : collectionValues) {
                if (((TelegramMensajeRaw) obj2).getId() > j4) {
                    arrayList.add(obj2);
                }
            }
            List<TelegramMensajeRaw> listSortedWith = CollectionsKt.sortedWith(arrayList, new Comparator() { // from class: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$sincronizarIncremental$2$invokeSuspend$$inlined$sortedBy$1
                /* JADX WARN: Multi-variable type inference failed */
                @Override // java.util.Comparator
                public final int compare(T t, T t2) {
                    return ComparisonsKt.compareValues(Long.valueOf(((TelegramMensajeRaw) t).getId()), Long.valueOf(((TelegramMensajeRaw) t2).getId()));
                }
            });
            ArrayList arrayList2 = new ArrayList();
            for (TelegramMensajeRaw telegramMensajeRaw2 : listSortedWith) {
                ReporteAfectaciones reporteAfectaciones = null;
                if (TelegramChannelFetcher.INSTANCE.esMensajeRelevante(telegramMensajeRaw2.getTexto())) {
                    ResultadoTraspasos resultadoTraspasosDetectar = Traspasos.INSTANCE.detectar(telegramMensajeRaw2.getTexto(), telegramMensajeRaw2.getFechaPublicacionMs());
                    String strQuitarOracionesDeTraspaso = Traspasos.INSTANCE.contieneIndicios(telegramMensajeRaw2.getTexto()) ? Traspasos.INSTANCE.quitarOracionesDeTraspaso(telegramMensajeRaw2.getTexto()) : telegramMensajeRaw2.getTexto();
                    ReporteAfectaciones reporteAfectacionesCopy = StringsKt.isBlank(strQuitarOracionesDeTraspaso) ? null : AfectacionesParser.INSTANCE.parsearMensajeTelegram(strQuitarOracionesDeTraspaso, telegramMensajeRaw2.getFechaPublicacionMs(), telegramMensajeRaw2.getId());
                    if (reporteAfectacionesCopy == null) {
                        ReporteAfectaciones reporteAfectaciones2 = AfectacionesParser.INSTANCE.parsearMensajeTelegram(telegramMensajeRaw2.getTexto(), telegramMensajeRaw2.getFechaPublicacionMs(), telegramMensajeRaw2.getId());
                        reporteAfectacionesCopy = reporteAfectaciones2.copy((32705 & 1) != 0 ? reporteAfectaciones2.tipo : null, (32705 & 2) != 0 ? reporteAfectaciones2.bloquesAfectados : CollectionsKt.emptyList(), (32705 & 4) != 0 ? reporteAfectaciones2.circuitosAfectados : CollectionsKt.emptyList(), (32705 & 8) != 0 ? reporteAfectaciones2.circuitosNormales : CollectionsKt.emptyList(), (32705 & 16) != 0 ? reporteAfectaciones2.eventosOrdenados : CollectionsKt.emptyList(), (32705 & 32) != 0 ? reporteAfectaciones2.eventosBloquesOrdenados : CollectionsKt.emptyList(), (32705 & 64) != 0 ? reporteAfectaciones2.descripcionOriginal : null, (32705 & 128) != 0 ? reporteAfectaciones2.fechaHoraTexto : null, (32705 & 256) != 0 ? reporteAfectaciones2.fechaPublicacionMs : 0L, (32705 & 512) != 0 ? reporteAfectaciones2.esRestablecimiento : false, (32705 & 1024) != 0 ? reporteAfectaciones2.causaAveria : null, (32705 & 2048) != 0 ? reporteAfectaciones2.mensajeId : 0L, (32705 & 4096) != 0 ? reporteAfectaciones2.duracionesMs : null, (32705 & 8192) != 0 ? reporteAfectaciones2.traspasos : null, (32705 & 16384) != 0 ? reporteAfectaciones2.traspasosNormalizados : null);
                    }
                    ReporteAfectaciones reporteAfectaciones3 = reporteAfectacionesCopy;
                    ReporteAfectaciones reporteAfectacionesCopy2 = reporteAfectaciones3.copy((32705 & 1) != 0 ? reporteAfectaciones3.tipo : null, (32705 & 2) != 0 ? reporteAfectaciones3.bloquesAfectados : null, (32705 & 4) != 0 ? reporteAfectaciones3.circuitosAfectados : null, (32705 & 8) != 0 ? reporteAfectaciones3.circuitosNormales : null, (32705 & 16) != 0 ? reporteAfectaciones3.eventosOrdenados : null, (32705 & 32) != 0 ? reporteAfectaciones3.eventosBloquesOrdenados : null, (32705 & 64) != 0 ? reporteAfectaciones3.descripcionOriginal : telegramMensajeRaw2.getTexto(), (32705 & 128) != 0 ? reporteAfectaciones3.fechaHoraTexto : null, (32705 & 256) != 0 ? reporteAfectaciones3.fechaPublicacionMs : 0L, (32705 & 512) != 0 ? reporteAfectaciones3.esRestablecimiento : false, (32705 & 1024) != 0 ? reporteAfectaciones3.causaAveria : null, (32705 & 2048) != 0 ? reporteAfectaciones3.mensajeId : 0L, (32705 & 4096) != 0 ? reporteAfectaciones3.duracionesMs : null, (32705 & 8192) != 0 ? reporteAfectaciones3.traspasos : resultadoTraspasosDetectar.getTraspasos(), (32705 & 16384) != 0 ? reporteAfectaciones3.traspasosNormalizados : resultadoTraspasosDetectar.getNormalizados());
                    if (!reporteAfectacionesCopy2.getCircuitosAfectados().isEmpty() || !reporteAfectacionesCopy2.getBloquesAfectados().isEmpty() || !reporteAfectacionesCopy2.getCircuitosNormales().isEmpty() || !reporteAfectacionesCopy2.getEventosOrdenados().isEmpty() || !resultadoTraspasosDetectar.getVacio()) {
                        reporteAfectaciones = reporteAfectacionesCopy2;
                    }
                }
                if (reporteAfectaciones != null) {
                    arrayList2.add(reporteAfectaciones);
                }
            }
            ArrayList arrayList3 = arrayList2;
            long j5 = this.$ultimoIdConocido;
            Long l = (Long) CollectionsKt.maxOrNull((Iterable) linkedHashMap.keySet());
            return new ResultadoSincronizacion(arrayList3, Math.max(j5, l != null ? l.longValue() : j), z3, z2);
        }
    }

    public static /* synthetic */ Object sincronizarIncremental$default(TelegramChannelFetcher telegramChannelFetcher, long j, int i, long j2, Continuation continuation, int i2, Object obj) {
        if ((i2 & 2) != 0) {
            i = 15;
        }
        int i3 = i;
        if ((i2 & 4) != 0) {
            j2 = System.currentTimeMillis();
        }
        return telegramChannelFetcher.sincronizarIncremental(j, i3, j2, continuation);
    }

    public final Object sincronizarIncremental(long j, int i, long j2, Continuation<? super ResultadoSincronizacion> continuation) {
        return BuildersKt.withContext(Dispatchers.getIO(), new C03382(i, j, j2, null), continuation);
    }

    /* JADX INFO: renamed from: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosComunicados$2, reason: invalid class name */
    /* JADX INFO: compiled from: TelegramChannelFetcher.kt */
    @Metadata(d1 = {"\u0000\u000e\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\u0010\u0000\u001a\b\u0012\u0004\u0012\u00020\u00020\u0001*\u00020\u0003H\n"}, d2 = {"<anonymous>", "", "Lcom/ermetic/circuitoshabana/data/ComunicadoModel;", "Lkotlinx/coroutines/CoroutineScope;"}, k = 3, mv = {2, 2, 0}, xi = AndroidUiModes.UI_MODE_NIGHT_MASK)
    @DebugMetadata(c = "com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosComunicados$2", f = "TelegramChannelFetcher.kt", i = {}, l = {}, m = "invokeSuspend", n = {}, s = {})
    static final class AnonymousClass2 extends SuspendLambda implements Function2<CoroutineScope, Continuation<? super List<? extends ComunicadoModel>>, Object> {
        int label;

        AnonymousClass2(Continuation<? super AnonymousClass2> continuation) {
            super(2, continuation);
        }

        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Continuation<Unit> create(Object obj, Continuation<?> continuation) {
            return new AnonymousClass2(continuation);
        }

        @Override // kotlin.jvm.functions.Function2
        public /* bridge */ /* synthetic */ Object invoke(CoroutineScope coroutineScope, Continuation<? super List<? extends ComunicadoModel>> continuation) {
            return invoke2(coroutineScope, (Continuation<? super List<ComunicadoModel>>) continuation);
        }

        /* JADX INFO: renamed from: invoke, reason: avoid collision after fix types in other method */
        public final Object invoke2(CoroutineScope coroutineScope, Continuation<? super List<ComunicadoModel>> continuation) {
            return ((AnonymousClass2) create(coroutineScope, continuation)).invokeSuspend(Unit.INSTANCE);
        }

        /* JADX WARN: Code duplicated, block: B:100:0x02d4 A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:103:0x02de A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:108:0x02fa A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:118:0x033a A[DONT_INVERT] */
        /* JADX WARN: Code duplicated, block: B:119:0x033c  */
        /* JADX WARN: Code duplicated, block: B:120:0x033f  */
        /* JADX WARN: Code duplicated, block: B:123:0x0350  */
        /* JADX WARN: Code duplicated, block: B:125:0x0358 A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:127:0x0365  */
        /* JADX WARN: Code duplicated, block: B:128:0x0369 A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:130:0x0378 A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:144:0x03b7  */
        /* JADX WARN: Code duplicated, block: B:170:0x011f A[SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:171:0x011f A[SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:175:0x02eb A[SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:176:0x02ea A[SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:177:? A[LOOP:3: B:101:0x02d8->B:177:?, LOOP_END, SYNTHETIC] */
        /* JADX WARN: Code duplicated, block: B:32:0x00db  */
        /* JADX WARN: Code duplicated, block: B:35:0x00ef A[Catch: Exception -> 0x016c, TryCatch #1 {Exception -> 0x016c, blocks: (B:23:0x00a1, B:28:0x00c6, B:30:0x00d3, B:33:0x00dd, B:35:0x00ef, B:37:0x010d, B:38:0x011f, B:42:0x012f, B:44:0x014e), top: B:156:0x00a1 }] */
        /* JADX WARN: Code duplicated, block: B:37:0x010d A[Catch: Exception -> 0x016c, TryCatch #1 {Exception -> 0x016c, blocks: (B:23:0x00a1, B:28:0x00c6, B:30:0x00d3, B:33:0x00dd, B:35:0x00ef, B:37:0x010d, B:38:0x011f, B:42:0x012f, B:44:0x014e), top: B:156:0x00a1 }] */
        /* JADX WARN: Code duplicated, block: B:55:0x01be A[Catch: Exception -> 0x0403, TRY_LEAVE, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:58:0x01f9 A[Catch: Exception -> 0x0403, TRY_ENTER, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:72:0x024a  */
        /* JADX WARN: Code duplicated, block: B:75:0x0252 A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:91:0x02af  */
        /* JADX WARN: Code duplicated, block: B:95:0x02c0 A[Catch: Exception -> 0x0403, TRY_ENTER, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        /* JADX WARN: Code duplicated, block: B:97:0x02ca A[Catch: Exception -> 0x0403, TryCatch #4 {Exception -> 0x0403, blocks: (B:50:0x0172, B:52:0x019a, B:53:0x01b8, B:55:0x01be, B:58:0x01f9, B:60:0x0205, B:62:0x0212, B:64:0x021f, B:66:0x022c, B:68:0x0239, B:73:0x024c, B:75:0x0252, B:77:0x025e, B:79:0x0268, B:81:0x0277, B:83:0x0284, B:85:0x0291, B:87:0x029e, B:92:0x02b1, B:95:0x02c0, B:97:0x02ca, B:106:0x02eb, B:108:0x02fa, B:110:0x0307, B:112:0x0314, B:114:0x0320, B:116:0x032d, B:121:0x0341, B:146:0x03bc, B:125:0x0358, B:128:0x0369, B:130:0x0378, B:133:0x0386, B:136:0x0397, B:100:0x02d4, B:101:0x02d8, B:103:0x02de), top: B:162:0x0172 }] */
        @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
        public final Object invokeSuspend(Object obj) {
            String str;
            boolean z;
            SimpleDateFormat simpleDateFormat;
            String lowerCase;
            ReporteAfectaciones reporteAfectaciones;
            boolean z2;
            boolean z3;
            boolean z4;
            String str2;
            String str3;
            String str4;
            List<EventoCircuito> eventosOrdenados;
            Iterator<T> it;
            String str5;
            String str6;
            Element elementFirst;
            String strAttr;
            long j;
            Element elementFirst2;
            String strText;
            String str7 = "/";
            String str8 = "nota informativa";
            String str9 = "get(...)";
            IntrinsicsKt.getCOROUTINE_SUSPENDED();
            if (this.label != 0) {
                throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");
            }
            ResultKt.throwOnFailure(obj);
            ArrayList arrayList = new ArrayList();
            ArrayList arrayList2 = new ArrayList();
            String str10 = TelegramChannelFetcher.TELEGRAM_CHANNEL_URL;
            boolean z5 = true;
            int i = 1;
            int size = 0;
            while (true) {
                if (i < 16 && size < 300) {
                    try {
                        Document document = Jsoup.connect(str10).userAgent(TelegramChannelFetcher.UA).timeout(10000).followRedirects(z5).get();
                        Intrinsics.checkNotNullExpressionValue(document, str9);
                        Elements elementsSelect = document.select("div.tgme_widget_message");
                        Intrinsics.checkNotNullExpressionValue(elementsSelect, "select(...)");
                        if (!elementsSelect.isEmpty()) {
                            ArrayList arrayList3 = new ArrayList();
                            int size2 = elementsSelect.size();
                            String str11 = "";
                            int i2 = 0;
                            while (i2 < size2) {
                                try {
                                    Element element = elementsSelect.get(i2);
                                    Intrinsics.checkNotNullExpressionValue(element, str9);
                                    Element element2 = element;
                                    if (i2 == 0) {
                                        String strAttr2 = element2.attr("data-post");
                                        Intrinsics.checkNotNullExpressionValue(strAttr2, "attr(...)");
                                        str5 = str7;
                                        str = str8;
                                        str6 = str9;
                                        try {
                                            if (StringsKt.contains$default((CharSequence) strAttr2, (CharSequence) str5, false, 2, (Object) null)) {
                                                z = true;
                                                try {
                                                    str11 = (String) CollectionsKt.last(StringsKt.split$default((CharSequence) strAttr2, new String[]{str5}, false, 0, 6, (Object) null));
                                                } catch (Exception e) {
                                                    e = e;
                                                    try {
                                                        Log.w(TelegramChannelFetcher.TAG, "Lote comunicados " + i + " falló: " + e.getMessage());
                                                        simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy hh:mm a", Locale.getDefault());
                                                        simpleDateFormat.setTimeZone(TimeZone.getTimeZone("America/Havana"));
                                                        for (TelegramMensajeRaw telegramMensajeRaw : CollectionsKt.takeLast(arrayList2, 300)) {
                                                            lowerCase = telegramMensajeRaw.getTexto().toLowerCase(Locale.ROOT);
                                                            Intrinsics.checkNotNullExpressionValue(lowerCase, "toLowerCase(...)");
                                                            reporteAfectaciones = AfectacionesParser.parsearMensajeTelegram$default(AfectacionesParser.INSTANCE, telegramMensajeRaw.getTexto(), telegramMensajeRaw.getFechaPublicacionMs(), 0L, 4, null);
                                                            if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null)) {
                                                                z2 = z;
                                                            } else {
                                                                z2 = z;
                                                            }
                                                            if (reporteAfectaciones.getEsRestablecimiento()) {
                                                                z3 = z;
                                                            } else {
                                                                z3 = z;
                                                            }
                                                            if (reporteAfectaciones.getCircuitosAfectados().isEmpty()) {
                                                                eventosOrdenados = reporteAfectaciones.getEventosOrdenados();
                                                                if (eventosOrdenados instanceof Collection) {
                                                                    it = eventosOrdenados.iterator();
                                                                    while (true) {
                                                                        if (it.hasNext()) {
                                                                            if (((EventoCircuito) it.next()).getEsAfectado()) {
                                                                            }
                                                                        } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afectó", false, 2, (Object) null)) {
                                                                        }
                                                                    }
                                                                } else {
                                                                    it = eventosOrdenados.iterator();
                                                                    while (true) {
                                                                        if (it.hasNext()) {
                                                                            if (((EventoCircuito) it.next()).getEsAfectado()) {
                                                                            }
                                                                        } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afectó", false, 2, (Object) null)) {
                                                                        }
                                                                    }
                                                                }
                                                                if (z3) {
                                                                    z4 = false;
                                                                } else {
                                                                    z4 = z;
                                                                }
                                                            } else if (z3) {
                                                                z4 = z;
                                                            } else {
                                                                z4 = false;
                                                            }
                                                            if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null)) {
                                                                str4 = "📢 Nota Informativa";
                                                            } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "comunicado", false, 2, (Object) null)) {
                                                                str4 = "📜 Comunicado Oficial";
                                                            } else {
                                                                if (!StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "actualización de afectaciones por déficit", false, 2, (Object) null)) {
                                                                    str2 = "⚡ Actualización de Déficit";
                                                                } else {
                                                                    str2 = "⚡ Actualización de Déficit";
                                                                }
                                                                str3 = str2;
                                                                String str12 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                                                                String str13 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                                                                Intrinsics.checkNotNull(str12);
                                                                arrayList.add(new ComunicadoModel(str13, str3, str12, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
                                                            }
                                                            str3 = str4;
                                                            String str14 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                                                            String str15 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                                                            Intrinsics.checkNotNull(str14);
                                                            arrayList.add(new ComunicadoModel(str15, str3, str14, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
                                                        }
                                                    } catch (Exception e2) {
                                                        Log.e(TelegramChannelFetcher.TAG, "Error obteniendo comunicados: " + e2.getMessage());
                                                    }
                                                    return CollectionsKt.sortedWith(arrayList, new Comparator() { // from class: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosComunicados$2$invokeSuspend$$inlined$sortedByDescending$1
                                                        /* JADX WARN: Multi-variable type inference failed */
                                                        @Override // java.util.Comparator
                                                        public final int compare(T t, T t2) {
                                                            return ComparisonsKt.compareValues(Long.valueOf(((ComunicadoModel) t2).getTimestampMs()), Long.valueOf(((ComunicadoModel) t).getTimestampMs()));
                                                        }
                                                    });
                                                }
                                            }
                                            elementFirst = element2.select("time.time, time").first();
                                            if (elementFirst != null || (strAttr = elementFirst.attr("datetime")) == null) {
                                                strAttr = "";
                                            }
                                            j = TelegramChannelFetcher.INSTANCE.parsearIsoDateTime(strAttr);
                                            elementFirst2 = element2.select("div.tgme_widget_message_text, .js-message_text").first();
                                            if (elementFirst2 != null) {
                                                elementFirst2.select("br").before("\n");
                                                strText = elementFirst2.text();
                                                Intrinsics.checkNotNullExpressionValue(strText, "text(...)");
                                                if (!StringsKt.isBlank(strText)) {
                                                    arrayList3.add(new TelegramMensajeRaw(strText, j, 0L, 4, null));
                                                }
                                            }
                                            i2++;
                                            z5 = z;
                                            str7 = str5;
                                            str8 = str;
                                            str9 = str6;
                                        } catch (Exception e3) {
                                            e = e3;
                                            z = true;
                                            Log.w(TelegramChannelFetcher.TAG, "Lote comunicados " + i + " falló: " + e.getMessage());
                                            simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy hh:mm a", Locale.getDefault());
                                            simpleDateFormat.setTimeZone(TimeZone.getTimeZone("America/Havana"));
                                            while (r2.hasNext()) {
                                                lowerCase = telegramMensajeRaw.getTexto().toLowerCase(Locale.ROOT);
                                                Intrinsics.checkNotNullExpressionValue(lowerCase, "toLowerCase(...)");
                                                reporteAfectaciones = AfectacionesParser.parsearMensajeTelegram$default(AfectacionesParser.INSTANCE, telegramMensajeRaw.getTexto(), telegramMensajeRaw.getFechaPublicacionMs(), 0L, 4, null);
                                                if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null)) {
                                                    z2 = z;
                                                } else {
                                                    z2 = z;
                                                }
                                                if (reporteAfectaciones.getEsRestablecimiento()) {
                                                    z3 = z;
                                                } else {
                                                    z3 = z;
                                                }
                                                if (reporteAfectaciones.getCircuitosAfectados().isEmpty()) {
                                                    eventosOrdenados = reporteAfectaciones.getEventosOrdenados();
                                                    if (eventosOrdenados instanceof Collection) {
                                                        it = eventosOrdenados.iterator();
                                                        while (true) {
                                                            if (it.hasNext()) {
                                                                if (((EventoCircuito) it.next()).getEsAfectado()) {
                                                                }
                                                            } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afectó", false, 2, (Object) null)) {
                                                            }
                                                        }
                                                    } else {
                                                        it = eventosOrdenados.iterator();
                                                        while (true) {
                                                            if (it.hasNext()) {
                                                                if (((EventoCircuito) it.next()).getEsAfectado()) {
                                                                }
                                                            } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afectó", false, 2, (Object) null)) {
                                                            }
                                                        }
                                                    }
                                                    if (z3) {
                                                        z4 = z;
                                                    } else {
                                                        z4 = false;
                                                    }
                                                } else if (z3) {
                                                    z4 = z;
                                                } else {
                                                    z4 = false;
                                                }
                                                if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null)) {
                                                    str4 = "📢 Nota Informativa";
                                                } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "comunicado", false, 2, (Object) null)) {
                                                    str4 = "📜 Comunicado Oficial";
                                                } else {
                                                    if (!StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "actualización de afectaciones por déficit", false, 2, (Object) null)) {
                                                        str2 = "⚡ Actualización de Déficit";
                                                    } else {
                                                        str2 = "⚡ Actualización de Déficit";
                                                    }
                                                    str3 = str2;
                                                    String str16 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                                                    String str17 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                                                    Intrinsics.checkNotNull(str16);
                                                    arrayList.add(new ComunicadoModel(str17, str3, str16, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
                                                }
                                                str3 = str4;
                                                String str18 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                                                String str19 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                                                Intrinsics.checkNotNull(str18);
                                                arrayList.add(new ComunicadoModel(str19, str3, str18, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
                                            }
                                            return CollectionsKt.sortedWith(arrayList, new Comparator() { // from class: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosComunicados$2$invokeSuspend$$inlined$sortedByDescending$1
                                                /* JADX WARN: Multi-variable type inference failed */
                                                @Override // java.util.Comparator
                                                public final int compare(T t, T t2) {
                                                    return ComparisonsKt.compareValues(Long.valueOf(((ComunicadoModel) t2).getTimestampMs()), Long.valueOf(((ComunicadoModel) t).getTimestampMs()));
                                                }
                                            });
                                        }
                                    } else {
                                        str5 = str7;
                                        str = str8;
                                        str6 = str9;
                                    }
                                    z = true;
                                    elementFirst = element2.select("time.time, time").first();
                                    if (elementFirst != null) {
                                        strAttr = "";
                                    } else {
                                        strAttr = "";
                                    }
                                    j = TelegramChannelFetcher.INSTANCE.parsearIsoDateTime(strAttr);
                                    elementFirst2 = element2.select("div.tgme_widget_message_text, .js-message_text").first();
                                    if (elementFirst2 != null) {
                                        elementFirst2.select("br").before("\n");
                                        strText = elementFirst2.text();
                                        Intrinsics.checkNotNullExpressionValue(strText, "text(...)");
                                        if (!StringsKt.isBlank(strText)) {
                                            arrayList3.add(new TelegramMensajeRaw(strText, j, 0L, 4, null));
                                        }
                                    }
                                    i2++;
                                    z5 = z;
                                    str7 = str5;
                                    str8 = str;
                                    str9 = str6;
                                } catch (Exception e4) {
                                    e = e4;
                                    str = str8;
                                }
                            }
                            String str20 = str7;
                            str = str8;
                            String str21 = str9;
                            z = z5;
                            arrayList2.addAll(0, arrayList3);
                            size += arrayList3.size();
                            String str22 = str11;
                            if (str22.length() <= 0) {
                                break;
                            }
                            str10 = "https://t.me/s/EmpresaElectricaDeLaHabana?before=" + str22;
                            i++;
                            z5 = z;
                            str7 = str20;
                            str8 = str;
                            str9 = str21;
                        }
                    } catch (Exception e5) {
                        e = e5;
                        str = str8;
                        z = z5;
                    }
                }
                str = str8;
                z = z5;
                break;
            }
            simpleDateFormat = new SimpleDateFormat("dd/MM/yyyy hh:mm a", Locale.getDefault());
            simpleDateFormat.setTimeZone(TimeZone.getTimeZone("America/Havana"));
            while (r2.hasNext()) {
                lowerCase = telegramMensajeRaw.getTexto().toLowerCase(Locale.ROOT);
                Intrinsics.checkNotNullExpressionValue(lowerCase, "toLowerCase(...)");
                reporteAfectaciones = AfectacionesParser.parsearMensajeTelegram$default(AfectacionesParser.INSTANCE, telegramMensajeRaw.getTexto(), telegramMensajeRaw.getFechaPublicacionMs(), 0L, 4, null);
                if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "comunicado", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "atención", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "atencion", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "información", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "informacion", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "aviso", false, 2, (Object) null)) {
                    z2 = z;
                } else {
                    z2 = false;
                }
                if (reporteAfectaciones.getEsRestablecimiento() || ((!reporteAfectaciones.getCircuitosNormales().isEmpty() && reporteAfectaciones.getCircuitosAfectados().isEmpty()) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "quedó restablecido", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "quedo restablecido", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "queda restablecido", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se restableció", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se restablecio", false, 2, (Object) null))) {
                    z3 = z;
                } else {
                    z3 = false;
                }
                if (reporteAfectaciones.getCircuitosAfectados().isEmpty()) {
                    eventosOrdenados = reporteAfectaciones.getEventosOrdenados();
                    if ((eventosOrdenados instanceof Collection) || !eventosOrdenados.isEmpty()) {
                        it = eventosOrdenados.iterator();
                        while (true) {
                            if (it.hasNext()) {
                                if (((EventoCircuito) it.next()).getEsAfectado()) {
                                }
                            }
                            if (z3) {
                                z4 = z;
                            } else {
                                z4 = false;
                            }
                        }
                    }
                    if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afectó", false, 2, (Object) null) && !StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "se afecto", false, 2, (Object) null) && !StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "disparo", false, 2, (Object) null) && !StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "trabajos operativos", false, 2, (Object) null) && !StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "déficit", false, 2, (Object) null) && !StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "deficit", false, 2, (Object) null)) {
                        z4 = false;
                    } else if (z3) {
                        z4 = z;
                    } else {
                        z4 = false;
                    }
                } else if (z3) {
                    z4 = z;
                } else {
                    z4 = false;
                }
                if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) str, false, 2, (Object) null)) {
                    str4 = "📢 Nota Informativa";
                } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "comunicado", false, 2, (Object) null)) {
                    str4 = "📜 Comunicado Oficial";
                } else {
                    if (!StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "actualización de afectaciones por déficit", false, 2, (Object) null) || StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "actualizacion de afectaciones por deficit", false, 2, (Object) null)) {
                        str2 = "⚡ Actualización de Déficit";
                    } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "disparo del circuito", false, 2, (Object) null)) {
                        str4 = "🚨 Aviso de Disparo";
                    } else if (StringsKt.contains$default((CharSequence) lowerCase, (CharSequence) "trabajos operativos", false, 2, (Object) null)) {
                        str2 = "🛠️ Trabajos Operativos";
                    } else if (z3) {
                        str2 = "🟢 Restablecimiento de Servicio";
                    } else if (z4) {
                        str2 = "🔴 Afectación de Servicio";
                    } else {
                        str2 = "📣 Comunicado Oficial";
                    }
                    str3 = str2;
                    String str110 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                    String str111 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                    Intrinsics.checkNotNull(str110);
                    arrayList.add(new ComunicadoModel(str111, str3, str110, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
                }
                str3 = str4;
                String str112 = simpleDateFormat.format(new Date(telegramMensajeRaw.getFechaPublicacionMs()));
                String str113 = telegramMensajeRaw.getFechaPublicacionMs() + "_" + telegramMensajeRaw.getTexto().hashCode();
                Intrinsics.checkNotNull(str112);
                arrayList.add(new ComunicadoModel(str113, str3, str112, telegramMensajeRaw.getFechaPublicacionMs(), telegramMensajeRaw.getTexto(), z2, z4, z3));
            }
            return CollectionsKt.sortedWith(arrayList, new Comparator() { // from class: com.ermetic.circuitoshabana.data.TelegramChannelFetcher$obtenerUltimosComunicados$2$invokeSuspend$$inlined$sortedByDescending$1
                /* JADX WARN: Multi-variable type inference failed */
                @Override // java.util.Comparator
                public final int compare(T t, T t2) {
                    return ComparisonsKt.compareValues(Long.valueOf(((ComunicadoModel) t2).getTimestampMs()), Long.valueOf(((ComunicadoModel) t).getTimestampMs()));
                }
            });
        }
    }

    public final Object obtenerUltimosComunicados(Continuation<? super List<ComunicadoModel>> continuation) {
        return BuildersKt.withContext(Dispatchers.getIO(), new AnonymousClass2(null), continuation);
    }
}
